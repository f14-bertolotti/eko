
from grammar import Parser

from pathlib import Path
import os

paths = set()

class Import:
    def __init__(self, transformer, path, name):
        assert Path(transformer.curr_path) not in paths, "circular import: {transformer.curr_path} was already imported."
        paths.add(Path(transformer.curr_path))
        self.path = os.path.join(os.path.dirname(transformer.curr_path), path)
        self.eko = self.load(self.path, transformer)

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
        return f"import {self.path} from aaa"
