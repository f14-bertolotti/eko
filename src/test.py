

from lark import Lark
from semantic import EkoTransformer

if __name__ == "__main__":
    with open("./src/grammar/grammar.lark") as grammar:
        echo_parser = Lark(grammar.read(), start="start")
    
        with open("./src/test/example.eko") as example:
            tree = echo_parser.parse(example.read())
            print(EkoTransformer().transform(tree))


