

class Key:

    def __init__(self, key, mod=None, ext=None):
        self.key = key
        self.mod = mod
        self.ext = ext

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return True if self.key == other.key else False

    def __ne__(self, other):
        return not (self == other)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "({},{},{})".format(self.key,
                                   self.mod if self.mod else "", 
                                   self.ext if self.ext else "")

