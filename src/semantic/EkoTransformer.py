from lark    import Transformer
from pathlib import Path

from .modifiers import Override
from .modifiers import Abstract
from .modifiers import Final

from .imports import Import

string2modifier = {
    "override" : Override,
    "abstract" : Abstract,
    "final"    : Final}

string2bool = {
    "true"  : True,
    "false" : False}

class EkoTransformer(Transformer):

    def modifier(self, mod):
        return string2modifier(str(mod))()

    def literal(self, l):
        (l,) = l
        return str(l)

    def string(self,s):
        (s,) = s
        return s[1:-1]

    def name(self, n):
        (n,) = n
        return str(n)

    def path(self, p):
        (p,) = p
        return Path(p)

    def integer(self, i):
        (i,) = i
        return int(i)

    def floating(self, f):
        (f,) = f
        return float(f)

    def none(self, _):
        return None

    def boolean(self, b):
        (b,) = b
        return string2bool[b]

    def assignement(self, kv):
        k,v = kv
        return k,v[0]

    def assignements(self, d):
        return dict(d)

    def value(self, f):
        return f

    def start(self, s):
        imports,name,dictionary = s
        return imports,{name:dictionary}

    def animport(self, path_cnf):
        (path,cnf) = path_cnf
        return Import(path, cnf)

    def imports(self, imports):
        return imports
