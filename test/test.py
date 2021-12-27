

from lark import Lark

with open("./grammar/grammer.ebnf") as grammar:
    echo_parser = Lark(grammar.read(), start="start")

    with open("./test/example.echo") as example:
        echo_parser.parse(example.read())


