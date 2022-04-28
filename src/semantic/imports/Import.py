
from grammar import Parser
from ..Key import Key
from pathlib import Path
import os

paths = set()

class Import:
    def __init__(self, transformer, path, name, alias):
        self.qualified_name = name
        self.alias = alias
        paths.add(Path(transformer.curr_path))
        self.path = os.path.join(os.path.dirname(transformer.curr_path), path)
        self.eko = self.load(self.path, transformer)

        self.is_valid()

    def __repr__(self):
        return str(self)

    def load(self, path, transformer):
        with open(path) as example:
            tree = Parser().parse(example.read())
            temp_path = transformer.curr_path
            transformer.curr_path = path
            eko = transformer.transform(tree)
            transformer.curr_path = temp_path
            return eko

    def __str__(self):
        return f"from {self.path} import {self.name} as {self.alias}"

    def is_valid(self):
        dictionary = self.eko.dictionary
        for name in self.qualified_name:
            if Key(name) not in dictionary: raise ValueError(f"could not resolve for {self.qualified_name}. Did not found {name}.")
            dictionary = dictionary[Key(name)]
        return True

