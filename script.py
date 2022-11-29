import glob
import os
import shutil
import subprocess
import tarfile
from os.path import exists

import requests
import yaml
from pyparsing import ParseResults

from protofile_parser import parsing_proto_package_directive, parsing_proto_service_name, \
    parsing_proto_imports_directive, parsing_proto_service


def get_proto_paths(proto_folders: list) -> list:
    """ Получаем пути до протофайлов """
    paths = set()
    for folder in proto_folders:
        paths_to_proto_files = glob.glob(f"{folder}/**/*.proto", recursive=True)
        for path in paths_to_proto_files:
            paths.add(path)
    return list(paths)


def create_uniq_name_for_client(package_directive: ParseResults, service_name: ParseResults) -> str:
    "Формируем уникальное имя для будущего клиента"
    package_directive = package_directive.replace('_', '.').split('.')
    package_directive = ''.join(name.title() for name in package_directive)
    return str(package_directive + service_name)


def clean_import_directives(imports_directive: ParseResults) -> list:
    """
    Получаем все импорты из протника. Забираем только те что являются внешней зависимостью и отсеиваем различные
    вендерные протники
    """
    external_dependencies = []
    for import_path in imports_directive:
        external_proto = import_path.asDict()['importPath']
        vendors_proto = ["google/api/annotations.proto", "google/protobuf/timestamp.proto",
                         "github.com/gogo/protobuf/gogoproto/gogo.proto", "google/protobuf/empty.proto",
                         "google/protobuf/wrappers.proto",
                         "github.com/envoyproxy/protoc-gen-validate/validate/validate.proto",
                         "google/protobuf/duration.proto", "google/protobuf/duration.struct",
                         "google/protobuf/descriptor.proto", "protoc-gen-openapiv2/options/annotations.proto",
                         "protoc-gen-openapiv2/options/openapiv2.proto"]
        if external_proto.replace('"', '') not in vendors_proto:
            external_dependencies.append(external_proto.replace('"', ''))
    return external_dependencies


def get_protofile_name(proto_path: str) -> str:
    """ получаем имя протофайла без .proto
    exmpl: 'api/v2/sc_v2.proto' -> 'sc_v2' """
    protofile_name = proto_path.split('/')[-1].removesuffix('.proto')
    if '-' in protofile_name:
        protofile_name = protofile_name.replace('-', '_')
    return protofile_name


def create_folder(package_name: str, folder_name: str):
    """ Создаем папку с именем протофайла внутри папки с именем пакета """
    os.makedirs(f'{package_name}/{folder_name}', exist_ok=True)


def get_external_proto_and_extract(path: str):
    """
    При помощи апихи мимира скачиваем протник который является зависимым и распаковываем архив
    """
    url = 'http://mimir.platform.prod.s.o3.ru/v1/vendor'
    headers = {"Content-Type": "application/json", "x-o3-sample-trace": "true"}
    data = {"dependencies":
                [{
                    "import_path": f"{path}",
                    "version": "master"
                }]}
    response = requests.post(url, headers=headers, json=data, stream=True)
    if response.status_code == 200:
        file = tarfile.open(fileobj=response.raw, mode="r|gz")
        file.extractall(path=".")
    else:
        print(response.status_code)
        print(response.content)


def copy_proto(_from: str, _to: str):
    """ Копируем протофайл из папки 'api' в специально подготовленную папку 'protofile_name' """
    shutil.copy(_from, _to)


def edit_proto_imports_for_external_dependencies(path_to_proto: str, external_path: str, package_name: str,
                                                 full_proto_name: str, protofile_name: str):
    """
    Редактируем импорт зависмового внешнего протника и делаем его локальным, указывая путь до папки куда мы
    скачали протник.
    """
    with open(f"{package_name}/{path_to_proto}", "rt") as file:
        data = file.read()
        data = data.replace(external_path, f"{package_name}/{protofile_name}/{full_proto_name}")

    with open(f"{package_name}/{path_to_proto}", "wt") as file:
        file.write(data)


def protoc_generate_pb_files(package_name: str, path_to_proto: str):
    """
    Генерируем пбшки для протника
    """
    cmd = f"python -m grpc_tools.protoc -I=.:vendor.pb --python_out=./{package_name}_setup/ --grpc_python_out=./{package_name}_setup/ ./{path_to_proto}"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    print('PROTOC OUTPUT: ', out)
    print('PROTOC ERROR: ', err)


def create_empty_init_recursively(package_name: str):
    file = "__init__.py"
    for dirpath, dirs, files in os.walk(f"./{package_name}_setup/{package_name}"):
        file_exists = os.path.exists(f"{dirpath}/{file}")
        if not file_exists:
            open(f"{dirpath}/{file}", 'a').close()


def generate_class(proto_name: str, uniq_class_name: str, service_name: ParseResults):
    """
    Тут создается класс будущего клиента. Он должен быть уникальным
    Так же указывается stub для сервиса
    """
    class_name_body = f"""
class {uniq_class_name}(BaseGrpc):
    grpc_stub = {proto_name}_pb2_grpc.{service_name}Stub
"""
    return class_name_body


def generate_imports(path_to_proto: str, proto_name: str, package_name: str):
    """
    Создаем импорты
    TODO: необходимо запилить проверку на Empty, чтобы там где нет пустых requests и response просто так не импортить
    Empty
    Так же вероятно нужно будет поместить BaseGrpc в отдельный пакет.
    """
    path_to_pb = package_name + "." + path_to_proto.replace("/", ".").replace("-", "_").removesuffix(f'.{proto_name}.proto')
    imports_body = f"""from ozwhc.grpc_clients import BaseGrpc
from {path_to_pb} import {proto_name}_pb2, {proto_name}_pb2_grpc
from google.protobuf.empty_pb2 import Empty

"""
    return imports_body


def change_method_name(name: str):
    """
    Вспомогательная функция для формирования читаемого имени метода
    """
    name = name['methodName']
    if 'ID' in name:
        name = name.replace('ID', 'Id')
    func_method_name = name[0].lower()
    for i in name[1:]:
        if i.isupper():
            func_method_name += f'_{i.lower()}'
        else:
            func_method_name += i
    return func_method_name


def generate_methods(methods: str, proto_name: str):
    """
    Тут формируются ручки
    """
    methods_body = """"""
    for method in methods:
        method_name = change_method_name(method)
        # проверка на наличие пустых реквестов и респонсов
        if 'google.protobuf.Empty' in method['methodRequest']:
            methods_body += f"""
    def {method_name}(self, request=Empty(), **kwargs) -> """
        else:
            methods_body += f"""
    def {method_name}(self, request: {proto_name}_pb2.{method['methodRequest']}, **kwargs) -> """

        if 'google.protobuf.Empty' in method['methodReturn']:
            methods_body += f"""Empty():"""
        else:
            methods_body += f"""{proto_name}_pb2.{method['methodReturn']}:"""

        # проверка на наличие стримов в методе
        if 'stream' in method:
            methods_body += f"""
        return self._grpc_stream(request=request, request_method=self.stub.{method['methodName']}, **kwargs)
            """
        else:
            methods_body += f"""
        return self._grpc_request(request=request, request_method=self.stub.{method['methodName']}, **kwargs)
                        """
    return methods_body


def fulfill_init_file(package_name: str, client_class_name: str, proto_name: str , methods: str, path_to_proto: str, service_name: ParseResults):
    """
    Эта функция по очереди собирает __init__ файл с клиентом для протника.
    generate_imports - создает импорты файла
    generate_class - создает класс клиента
    generate_methods - создает ручки для клиента
    Затем создается __init__ файл со всем содержимым.
    """
    init_body = """"""
    init_body += generate_imports(path_to_proto, proto_name, package_name)
    init_body += generate_class(proto_name, client_class_name, service_name)
    init_body += generate_methods(methods, proto_name)
    path_to_package_file = f'{package_name}_setup/{package_name}/{path_to_proto.replace("-", "_").removesuffix(f"{proto_name}.proto")}'
    with open(f"{path_to_package_file}__init__.py", "w") as file:
        file.write(init_body)


def generate_init_file_for_pypi_package(parsed_data: ParseResults, client_class_name: str, package_name: str, proto_name: str, path_to_proto: str, service_name: ParseResults):
    """
    Данная функция предназначена для создания клиента, который будет помещен в файл __init__ рядом с сгенерированными
    пбшками.
    """
    for service in parsed_data:
        service_as_dict = service.asDict()
        if 'serviceName' in service_as_dict and 'serviceMethods' in service_as_dict:
                methods = service_as_dict['serviceMethods']
                fulfill_init_file(package_name, client_class_name, proto_name, methods, path_to_proto, service_name)
        else:
            print("SERVICE NOT PARSED")
            break


def read_yaml(yaml_path: str) -> list:
    """ Читаем пути в файле yaml файлах """
    with open(yaml_path) as file:
        paths = yaml.safe_load(file)
    return paths['proto_paths']


def create_folder_and_copy_proto(package_name: str, path_to_proto: str):
    """ Копируем протник из оригинального местонахождения в проекте в папку с названием package_name при этом
    сохраняя всю оригинальную вложенность папок до протника
    """
    dst = f"{package_name}/{path_to_proto}"
    dst_folder = os.path.dirname(dst)
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)
    shutil.copy(path_to_proto, dst)


# имя пакета которое получаем через PY_CLI_PACKAGE_NAME
# py_cli_package_name = 'qa_whc_go_service_resource_limiter_grpc_client'
py_cli_package_name = 'qa_split_grpc_client'
# Вытаскиваем из мимира пути до протников
if exists('mimir.yaml'):
    proto_folders = read_yaml(yaml_path='mimir.yaml')
elif exists('.protogen.yaml'):
    proto_folders = read_yaml(yaml_path='.protogen.yaml')
else:
    raise AssertionError('There are not mimir.yaml and .protogen.yaml')
# дальше нужно получить все пути к протникам при помощи glob
proto_paths = get_proto_paths(proto_folders=proto_folders)
# создаем папку в которую будем копировать протники из проекта
os.makedirs(py_cli_package_name, exist_ok=True)
# создаем папку в которую будем генерировать пбшки
os.makedirs(f'{py_cli_package_name}_setup', exist_ok=True)

# итерируемся по каждому протнику
for path_to_proto in proto_paths:
    print('!!!', path_to_proto)
    # открываем протник
    with open(path_to_proto, 'r') as f:
        # считываем тело протника целиком
        proto_body = f.read()
        # парсим имя сервиса в протнике. оно тоже пригодится для формирования уникального имени
        service_name = parsing_proto_service_name(proto_body=proto_body)
        if service_name:
            # копируем протник в директорию py_cli_package_name с сохранением изначальной структуры
            create_folder_and_copy_proto(package_name=py_cli_package_name, path_to_proto=path_to_proto)
            # получаем имя протника без .proto
            clear_protofile_name = get_protofile_name(proto_path=path_to_proto)
            # парсим директиву package из протника. будем ее использовать для формирования уникального имени клиента
            package_directive = parsing_proto_package_directive(proto_body=proto_body)
            # формируем уникальное имя класса для будущего клиента
            uniq_client_name = create_uniq_name_for_client(package_directive, service_name)
            # парсим директиву импортов, чтобы найти внешние зависимости
            import_directives = parsing_proto_imports_directive(proto_body=proto_body)
            # ищем внешние зависимости отсеивая их от всяких валидаторов и gogo и envyproxy
            # если такие зависимости были найдены то проваливаемся по очереди в каждую из них
            if external_dependencies := clean_import_directives(imports_directive=import_directives):
                # идем по каждой такой зависимости, обычно это какой-нибудь constants.proto
                for external_path in external_dependencies:
                    # получаем полное имя протника вместе с расширением типа constants.proto
                    external_full_proto_name = external_path.split('/')[-1]
                    # получаем имя протника без расширения .proto
                    external_clear_protofile_name = get_protofile_name(proto_path=external_path)
                    # создаем папку в которую положим этот внешнмй протник. папка называется по имени протника
                    create_folder(package_name=py_cli_package_name, folder_name=external_clear_protofile_name)
                    # получаем внешний протник через ручку mimir и извлекаем его из архива
                    get_external_proto_and_extract(path=external_path)
                    # копируем полученный протник в папку которую создали выше
                    copy_proto(_from=f"./{external_path}",
                               _to=f"./{py_cli_package_name}/{external_clear_protofile_name}/{external_full_proto_name}")
                    # теперь в основном протнике радактируем импорт и указываем путь до только что полученного зависимого протника
                    edit_proto_imports_for_external_dependencies(path_to_proto=path_to_proto, external_path=external_path,
                                                                 package_name=py_cli_package_name,
                                                                 full_proto_name=external_full_proto_name,
                                                                 protofile_name=external_clear_protofile_name)
                    # теперь генерируем пбшки для этого зависимого протника
                    protoc_generate_pb_files(package_name=py_cli_package_name,
                                             path_to_proto=f"{py_cli_package_name}/{external_clear_protofile_name}/{external_full_proto_name}")

            # после того как мы проверили, есть ли у протника зависимости, мы генерим пбшки для этого протника
            protoc_generate_pb_files(package_name=py_cli_package_name,
                                     path_to_proto=f"{py_cli_package_name}/{path_to_proto}")
            # а теперь парсим в самом протнике секцию service для того чтобы получить все ручки
            parsed_data = parsing_proto_service(proto_body=proto_body)
            # на основе всех полученных данных мы формируем клиент, который будет находится в __ini__ файле
            generate_init_file_for_pypi_package(parsed_data=parsed_data,
                                                client_class_name=uniq_client_name,
                                                package_name=py_cli_package_name,
                                                proto_name=clear_protofile_name,
                                                path_to_proto=path_to_proto,
                                                service_name=service_name)

# создаем пустые файлы __init__ там где их нет, чтобы пакет сформировался корректно
create_empty_init_recursively(package_name=py_cli_package_name)
