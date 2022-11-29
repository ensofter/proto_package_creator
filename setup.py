from setuptools import setup, find_packages
from pkg_resources import FileMetadata
import os
from email import message_from_string


# if os.getenv('PY_CLI_PACKAGE_NAME') and os.getenv('PACKAGE_VERSION'):
#     service_name = os.getenv('PY_CLI_PACKAGE_NAME')
#     service_version = os.getenv('PACKAGE_VERSION')
# else:
#     # данная часть нужна для тестирования на совместимость.
#     pkg_info = FileMetadata('PKG-INFO')
#     pkg_info_data = message_from_string(pkg_info.get_metadata('PKG-INFO'))
#     service_name = pkg_info_data['name']
#     service_version = pkg_info_data['version']

setup(
    name=f"qa_batching_manager_grpc_client",
    version=f"1.33.0",
    keywords=("whc", "ozon", "qa", "grpc"),
    description=f"PyPi package for qa_batching_manager_grpc_client service",
    long_description="grpc package for python",
    url=f"ozon",
    author=f"ozon",
    author_email=f"ozon",
    packages=find_packages()
)
