from pyparsing import Word, alphas, alphanums, Regex, Suppress, Forward, Group, oneOf, ZeroOrMore, Optional, \
    delimitedList, Keyword, restOfLine, quotedString, Dict, OneOrMore, nums, SkipTo, tokenMap, ParseResults, \
    AtStringStart, Literal, LineStart


ident = Word(alphas + "_", alphanums + "_").setName("identifier")
integer = Regex(r"[+-]?\d+")

LBRACE = Suppress('{')
RBRACE = Suppress('}')
LBRACK = Suppress('[')
RBRACK = Suppress(']')
LPAR = Suppress('(')
RPAR = Suppress(')')
EQ = Suppress('=')
SEMI = Suppress(';')
COLON = Suppress(':')

RPC_ = Keyword('rpc')
RETURNS_ = Keyword('returns')
SERVICE_ = Literal('service')
OPTION_ = Keyword('option')
BODY_ = Keyword('body')
STREAM_ = Keyword('stream')
PACKAGE_ = Keyword('package')
IMPORT_ = Keyword('import')

TRUE_ = Keyword('true')

comment = '//' + restOfLine


def parsing_proto_service(proto_body: str) -> ParseResults:
    """
    Парсим всю директиву service для того чтобы получить все имеющиеся ручки
    """
    rpc_method = Keyword('post') | Keyword('get') | Keyword('patch') | Keyword('delete') | Keyword('put') | \
                 Keyword('operation_id') | Keyword('body')

    optionBody = (
            rpc_method
            + COLON
            + quotedString("endpointString")
            + Optional(',')
            + Optional(
                rpc_method
                + COLON
                + quotedString('*')
            )
    )

    optionDefn = (
            Optional(
                OPTION_
                + ident
                + EQ
                + TRUE_
                + SEMI
            )
            +
            Optional(
                OPTION_
                + LPAR
                + delimitedList(ident, '.', combine=True)
                + RPAR
                + EQ
                + LBRACE
                + Group(optionBody)('option body')
                + RBRACE
                + SEMI
            )
            +
            Optional(
                OPTION_
                + ident
                + EQ
                + TRUE_
                + SEMI
            )
            +
            Optional(
                OPTION_
                + LPAR
                + delimitedList(ident, '.', combine=True)
                + RPAR
                + EQ
                + LBRACE
                + Group(optionBody)('option body')
                + RBRACE
                + SEMI
            )
    )

    methodDefn = (
            RPC_
            - ident("methodName")
            + LPAR
            + delimitedList(ident, '.', combine=True)("methodRequest")
            + RPAR
            + RETURNS_
            + LPAR
            + (Optional(STREAM_)('stream') + delimitedList(ident, '.', combine=True)("methodReturn"))
            + RPAR
            + Optional(
                LBRACE
                + Group(optionDefn)('option')
                + RBRACE
            )
            + Optional(SEMI)
    )

    serviceDefn = (
            LineStart() + SERVICE_
            - ident.setResultsName('serviceName')
            + LBRACE
            + ZeroOrMore(Group(methodDefn))('serviceMethods')
            + RBRACE
    )

    serviceDefn.ignore(comment)

    result_of_parsing = serviceDefn.searchString(proto_body)

    return result_of_parsing


def parsing_proto_package_directive(proto_body: str) -> ParseResults:
    """
    Парсим директиву package внутри протника для того чтобы сформировать потом уникальное имя класса для
    будущего клиента.
    """
    packageDirective = (
            PACKAGE_
            - delimitedList(ident, '.', combine=True)('PackageString')
            + SEMI
    )
    packageDirective.ignore(comment)
    result_of_parsing = packageDirective.searchString(proto_body)
    return result_of_parsing[0].asDict()['PackageString']


def parsing_proto_service_name(proto_body: str):
    """
    Парсим имя сервиса внутри протника
    """
    serviceName = (
            LineStart() + SERVICE_
            - ident.setResultsName('serviceName')
    )
    serviceName.ignore(comment)
    result_of_parsing = serviceName.searchString(proto_body)
    if result_of_parsing:
        return result_of_parsing[0].asDict()['serviceName']
    return result_of_parsing


def parsing_proto_imports_directive(proto_body: str):
    """
    Парсим импорты внутри протника
    """
    importDirective = (
            IMPORT_ - quotedString.setResultsName('importPath') + SEMI
    )
    importDirective.ignore(comment)
    result_of_parsing = importDirective.searchString(proto_body)
    return result_of_parsing
