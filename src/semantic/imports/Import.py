
from grammar import Parser

class Import:
    def __init__(self, path, name):
        self.path = path
        self.name = name

    def __repr__(self):
        return str(self)

    def load(self):
        print(load)

    def __str__(self):
        return f"import {self.path} from {self.name}"
