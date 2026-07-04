# Generated from Expr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,5,9,2,0,7,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,7,0,2,1,
        0,0,0,2,3,5,1,0,0,3,4,5,2,0,0,4,5,5,4,0,0,5,6,5,3,0,0,6,7,5,0,0,
        1,7,1,1,0,0,0,0
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Print'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "PRINT", "P1", "P2", "CADENA", "WS" ]

    RULE_root = 0

    ruleNames =  [ "root" ]

    EOF = Token.EOF
    PRINT=1
    P1=2
    P2=3
    CADENA=4
    WS=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(ExprParser.PRINT, 0)

        def P1(self):
            return self.getToken(ExprParser.P1, 0)

        def CADENA(self):
            return self.getToken(ExprParser.CADENA, 0)

        def P2(self):
            return self.getToken(ExprParser.P2, 0)

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_root




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(ExprParser.PRINT)
            self.state = 3
            self.match(ExprParser.P1)
            self.state = 4
            self.match(ExprParser.CADENA)
            self.state = 5
            self.match(ExprParser.P2)
            self.state = 6
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





