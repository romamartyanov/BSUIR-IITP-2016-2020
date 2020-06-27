import os
import sys

import texttable as tt

from src.lexer import Lexer
from src.parser import Parser
from src.vm import GLOBAL, execute


def lab_2(args, tokens):
    if "lab_2" in args:
        tab = tt.Texttable()
        headings = ['Value (token)', 'Tag', 'Row', 'Column']
        tab.header(headings)

        values = list()
        tags = list()
        rows = list()
        columns = list()

        for token in tokens:
            values.append(token.value)
            tags.append(token.tag)
            rows.append(token.row)
            columns.append(token.col)

        for row in zip(values, tags, rows, columns):
            tab.add_row(row)
        s = tab.draw()
        print(s)


def lab_3(args, ast, tabs):
    if "lab_3" in args:
        for i in ast:
            if isinstance(i, list):
                lab_3(args, i, tabs + 1)
            else:
                result = tabs * '  |'
                print('{}{}'.format(result, i.value))


def lab_4(args):
    if "lab_4" in args:
        tab = tt.Texttable()
        headings = ['Variable', 'Type']
        tab.header(headings)

        variables = list()
        types = list()

        for key, value in GLOBAL.items():
            if isinstance(value, int) or isinstance(value, str):
                variables.append(key)
                types.append(type(value))

        for row in zip(variables, types):
            tab.add_row(row)
        s = tab.draw()
        print(s)


def main(args):
    """
    main

    """

    path = args[0]
    if len(path) > 1:
        if not os.path.exists(path):
            print('Error! File "%s" not found!' % path)
            exit(1)
    else:
        print('Error! Expected file, but given nothing!')
        exit(1)

    args = args[1:]

    lexer = Lexer(path)
    parser = Parser()
    tokens = lexer.tokens()

    if lexer.errors_list:
        lexer.errors()

    lab_2(args, tokens)

    try:
        ast = parser.build(tokens)
        lab_3(args, ast, 3)

        """ Lab 5 """
        for i in ast:
            execute(i, GLOBAL)

        lab_4(args)

    except Exception as ex:
        print(ex)
        exit(1)


if __name__ == '__main__':
    main(sys.argv[1:])
