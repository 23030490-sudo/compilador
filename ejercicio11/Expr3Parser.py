# Generated from Expr3.g4 by ANTLR 4.13.2
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
        4,1,21,15,2,0,7,0,2,1,7,1,1,0,5,0,6,8,0,10,0,12,0,9,9,0,1,0,1,0,
        1,1,1,1,1,1,0,0,2,0,2,0,1,1,0,1,20,13,0,7,1,0,0,0,2,12,1,0,0,0,4,
        6,3,2,1,0,5,4,1,0,0,0,6,9,1,0,0,0,7,5,1,0,0,0,7,8,1,0,0,0,8,10,1,
        0,0,0,9,7,1,0,0,0,10,11,5,0,0,1,11,1,1,0,0,0,12,13,7,0,0,0,13,3,
        1,0,0,0,1,7
    ]

class Expr3Parser ( Parser ):

    grammarFileName = "Expr3.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'public'", "'class'", "'static'", "'void'", 
                     "'String'", "'int'", "'System'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'='", "'+'", "'.'", "';'", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "PUBLIC", "CLASS", "STATIC", "VOID", 
                      "STRING", "INT", "SYSTEM", "ID", "CADENA", "NUM", 
                      "ASIGNACION", "MAS", "PUNTO", "PC", "PARENTESIS1", 
                      "PARENTESIS2", "LLAVE1", "LLAVE2", "CORCHETE1", "CORCHETE2", 
                      "WS" ]

    RULE_root = 0
    RULE_elemento = 1

    ruleNames =  [ "root", "elemento" ]

    EOF = Token.EOF
    PUBLIC=1
    CLASS=2
    STATIC=3
    VOID=4
    STRING=5
    INT=6
    SYSTEM=7
    ID=8
    CADENA=9
    NUM=10
    ASIGNACION=11
    MAS=12
    PUNTO=13
    PC=14
    PARENTESIS1=15
    PARENTESIS2=16
    LLAVE1=17
    LLAVE2=18
    CORCHETE1=19
    CORCHETE2=20
    WS=21

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

        def EOF(self):
            return self.getToken(Expr3Parser.EOF, 0)

        def elemento(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Expr3Parser.ElementoContext)
            else:
                return self.getTypedRuleContext(Expr3Parser.ElementoContext,i)


        def getRuleIndex(self):
            return Expr3Parser.RULE_root




    def root(self):

        localctx = Expr3Parser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2097150) != 0):
                self.state = 4
                self.elemento()
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 10
            self.match(Expr3Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUBLIC(self):
            return self.getToken(Expr3Parser.PUBLIC, 0)

        def CLASS(self):
            return self.getToken(Expr3Parser.CLASS, 0)

        def STATIC(self):
            return self.getToken(Expr3Parser.STATIC, 0)

        def VOID(self):
            return self.getToken(Expr3Parser.VOID, 0)

        def STRING(self):
            return self.getToken(Expr3Parser.STRING, 0)

        def INT(self):
            return self.getToken(Expr3Parser.INT, 0)

        def SYSTEM(self):
            return self.getToken(Expr3Parser.SYSTEM, 0)

        def ID(self):
            return self.getToken(Expr3Parser.ID, 0)

        def CADENA(self):
            return self.getToken(Expr3Parser.CADENA, 0)

        def NUM(self):
            return self.getToken(Expr3Parser.NUM, 0)

        def ASIGNACION(self):
            return self.getToken(Expr3Parser.ASIGNACION, 0)

        def MAS(self):
            return self.getToken(Expr3Parser.MAS, 0)

        def PUNTO(self):
            return self.getToken(Expr3Parser.PUNTO, 0)

        def PC(self):
            return self.getToken(Expr3Parser.PC, 0)

        def PARENTESIS1(self):
            return self.getToken(Expr3Parser.PARENTESIS1, 0)

        def PARENTESIS2(self):
            return self.getToken(Expr3Parser.PARENTESIS2, 0)

        def LLAVE1(self):
            return self.getToken(Expr3Parser.LLAVE1, 0)

        def LLAVE2(self):
            return self.getToken(Expr3Parser.LLAVE2, 0)

        def CORCHETE1(self):
            return self.getToken(Expr3Parser.CORCHETE1, 0)

        def CORCHETE2(self):
            return self.getToken(Expr3Parser.CORCHETE2, 0)

        def getRuleIndex(self):
            return Expr3Parser.RULE_elemento




    def elemento(self):

        localctx = Expr3Parser.ElementoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_elemento)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2097150) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





