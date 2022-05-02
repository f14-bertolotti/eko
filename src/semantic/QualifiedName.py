

class QualifiedName:

    def __init__(self, *names):
        self.names = list(names)

    def __iter__(self):
        return iter(self.names)

    def __repr__(self): return str(self)
    def __str__(self):
        return ".".join([f"{name}" for name in self.names])

