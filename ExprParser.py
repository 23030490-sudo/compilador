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
        4,1,7,11,2,0,7,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,
        9,0,2,1,0,0,0,2,3,5,1,0,0,3,4,5,5,0,0,4,5,5,2,0,0,5,6,5,3,0,0,6,
        7,5,4,0,0,7,8,5,6,0,0,8,9,5,0,0,1,9,1,1,0,0,0,0
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "<INVALID>", "'>'", "<INVALID>", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "IF", "ID", "MAYORQUE", "NUM", "P1", 
                      "P2", "WS" ]

    RULE_root = 0

    ruleNames =  [ "root" ]

    EOF = Token.EOF
    IF=1
    ID=2
    MAYORQUE=3
    NUM=4
    P1=5
    P2=6
    WS=7

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

        def IF(self):
            return self.getToken(ExprParser.IF, 0)

        def P1(self):
            return self.getToken(ExprParser.P1, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def MAYORQUE(self):
            return self.getToken(ExprParser.MAYORQUE, 0)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

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
            self.match(ExprParser.IF)
            self.state = 3
            self.match(ExprParser.P1)
            self.state = 4
            self.match(ExprParser.ID)
            self.state = 5
            self.match(ExprParser.MAYORQUE)
            self.state = 6
            self.match(ExprParser.NUM)
            self.state = 7
            self.match(ExprParser.P2)
            self.state = 8
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





