
class Name:

    def __init__(self, name):
        if type(name) is not str: raise ValueError("name expects a string. Found {name}")
        self.name = name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return self.name != other.name

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.name}"
