# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,6,44,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,1,0,1,0,1,0,1,0,1,0,1,1,4,1,21,8,1,11,1,12,1,22,1,2,1,2,5,2,27,
        8,2,10,2,12,2,30,9,2,1,2,1,2,1,3,1,3,1,4,1,4,1,5,4,5,39,8,5,11,5,
        12,5,40,1,5,1,5,1,28,0,6,1,1,3,2,5,3,7,4,9,5,11,6,1,0,2,2,0,65,90,
        97,122,3,0,9,10,13,13,32,32,46,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,
        0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,1,13,1,0,0,0,3,20,1,0,0,0,
        5,24,1,0,0,0,7,33,1,0,0,0,9,35,1,0,0,0,11,38,1,0,0,0,13,14,5,112,
        0,0,14,15,5,114,0,0,15,16,5,105,0,0,16,17,5,110,0,0,17,18,5,116,
        0,0,18,2,1,0,0,0,19,21,7,0,0,0,20,19,1,0,0,0,21,22,1,0,0,0,22,20,
        1,0,0,0,22,23,1,0,0,0,23,4,1,0,0,0,24,28,5,34,0,0,25,27,9,0,0,0,
        26,25,1,0,0,0,27,30,1,0,0,0,28,29,1,0,0,0,28,26,1,0,0,0,29,31,1,
        0,0,0,30,28,1,0,0,0,31,32,5,34,0,0,32,6,1,0,0,0,33,34,5,61,0,0,34,
        8,1,0,0,0,35,36,5,59,0,0,36,10,1,0,0,0,37,39,7,1,0,0,38,37,1,0,0,
        0,39,40,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,42,1,0,0,0,42,43,
        6,5,0,0,43,12,1,0,0,0,4,0,22,28,40,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PRINT = 1
    ID = 2
    CADENA = 3
    IGUAL = 4
    PC = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'print'", "'='", "';'" ]

    symbolicNames = [ "<INVALID>",
            "PRINT", "ID", "CADENA", "IGUAL", "PC", "WS" ]

    ruleNames = [ "PRINT", "ID", "CADENA", "IGUAL", "PC", "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


