
from grammar.parser import Lark_StandAlone   as Parser
from grammar.parser import Transformer       as Transformer
from grammar.parser import InlineTransformer as InlineTransformer
from grammar.parser import v_args            as inlineargs

inlineargs = inlineargs(inline=True)
