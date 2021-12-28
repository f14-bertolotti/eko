

from grammar  import Parser
from semantic import EkoTransformer

if __name__ == "__main__":
    with open("./src/grammar/grammar.lark") as grammar:
        eko = Parser()
    
        with open("./src/test/example.eko") as example:
            tree = eko.parse(example.read())
            print(EkoTransformer().transform(tree))


