from grammar import InlineTransformer
from grammar import inlineargs
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


class EkoTransformer(InlineTransformer):

    def literal       ( self, literal                   ) : return str(literal)
    def name          ( self, name                      ) : return str(name)
    def integer       ( self, interger                  ) : return int(interger)
    def string        ( self, string                    ) : return str(string)
    def value         ( self, value                     ) : return value
    def imports       ( self, imports                   ) : return imports
    def floating      ( self, floating                  ) : return floating
    def path          ( self, path                      ) : return Path(path)
    def none          ( self                            ) : return None
    def modifier      ( self, modifier                  ) : return string2modifier[str(modifier)]()
    def quoted_string ( self, string                    ) : return string[1:-1]
    def boolean       ( self, b                         ) : return string2bool[b]
    def assignement   ( self, k, v                      ) : return k,v
    def animport      ( self, path, cnf                 ) : return Import(path, cnf)
    def assignements  ( self, *args                     ) : return dict(args)
    def start         ( self, imports, name, dictionary ) : return imports,{name:dictionary}

