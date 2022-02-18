from grammar import InlineTransformer
from grammar import inlineargs
from pathlib import Path

from .modifiers import Override
from .modifiers import Abstract
from .modifiers import Final

from .imports import Import
from .Eko import Eko
from .Key import Key


class EkoTransformer(InlineTransformer):

    # GROUND TERMINALS ##############
    def true    (self) : return True
    def false   (self) : return False
    def none    (self) : return None
    def override(self) : return Override()
    def abstract(self) : return Abstract()
    def final   (self) : return Final()

    # REGEX TERMINALS #######################################
    def literal       (self, literal ) : return str(literal)
    def name          (self, name    ) : return str(name)
    def integer       (self, interger) : return int(interger)
    def boolean       (self, boolean ) : return boolean
    def string        (self, string  ) : return str(string)
    def value         (self, value   ) : return value
    def floating      (self, floating) : return float(floating)
    def path          (self, path    ) : return Path(path)
    def quoted_string (self, string  ) : return string[1:-1]
    def modifier      (self, modifier) : return modifier
  
    # ASSIGNEMENTS ######################################################
    def smpl_assign     (self, k, v      ) : return Key(k),v
    def mdfr_assign     (self, m, k, v   ) : return Key(k,mod=m),v
    def xtnd_assign     (self, k, e, v   ) : return Key(k,ext=e),v
    def xtnd_mdfr_assign(self, m, k, e, v) : return Key(k,mod=m,ext=e),v
    def single_assign   (self, assign    ) : return assign
    def list_assign     (self, *args     ) : return dict(args)
    def first_assign    (self, assign    ) : return Eko(None, {assign[0]:assign[1]})

    def imports            (self, imports        ) : return imports
    def animport           (self, path, name     ) : return Import(self, path, name)
    def imports_with_assign(self, imports, assign) : return Eko(imports,{assign[0]:assign[1]})
    def start              (self, code           ) : return code

