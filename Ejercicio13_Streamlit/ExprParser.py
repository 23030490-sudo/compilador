# Generated from c:/Users/joseq/LYA2/compilador/Ejercicio13_Streamlit/Expr.g4 by ANTLR 4.13.1
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
        4,1,29,10,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,0,0,2,0,2,0,0,
        7,0,4,1,0,0,0,2,7,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,
        8,5,0,0,1,8,3,1,0,0,0,0
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'CREATE'", "'TABLE'", "'SERIAL'", "'PRIMARY'", 
                     "'KEY'", "'VARCHAR'", "'NOT'", "'NULL'", "'INTEGER'", 
                     "'DATE'", "'INSERT'", "'INTO'", "'VALUES'", "'SELECT'", 
                     "'FROM'", "'INNER'", "'JOIN'", "'ON'", "'WHERE'", "'='", 
                     "';'", "'('", "')'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "CREATE", "TABLE", "SERIAL", "PRIMARY", 
                      "KEY", "VARCHAR", "NOT", "NULL", "INTEGER", "DATE", 
                      "INSERT", "INTO", "VALUES", "SELECT", "FROM", "INNER", 
                      "JOIN", "ON", "WHERE", "IGUAL", "PUNTO_COMA", "PAR_A", 
                      "PAR_C", "COMA", "PUNTO", "ID", "NUM", "STRING_LIT", 
                      "WS" ]

    RULE_root = 0
    RULE_expr = 1

    ruleNames =  [ "root", "expr" ]

    EOF = Token.EOF
    CREATE=1
    TABLE=2
    SERIAL=3
    PRIMARY=4
    KEY=5
    VARCHAR=6
    NOT=7
    NULL=8
    INTEGER=9
    DATE=10
    INSERT=11
    INTO=12
    VALUES=13
    SELECT=14
    FROM=15
    INNER=16
    JOIN=17
    ON=18
    WHERE=19
    IGUAL=20
    PUNTO_COMA=21
    PAR_A=22
    PAR_C=23
    COMA=24
    PUNTO=25
    ID=26
    NUM=27
    STRING_LIT=28
    WS=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_root




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr()
            self.state = 5
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





