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
        4,1,6,29,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,0,1,0,1,1,1,1,3,1,18,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,
        1,3,1,3,0,0,4,0,2,4,6,0,0,26,0,9,1,0,0,0,2,17,1,0,0,0,4,19,1,0,0,
        0,6,24,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,11,1,0,0,0,11,9,1,0,0,
        0,11,12,1,0,0,0,12,13,1,0,0,0,13,14,5,0,0,1,14,1,1,0,0,0,15,18,3,
        4,2,0,16,18,3,6,3,0,17,15,1,0,0,0,17,16,1,0,0,0,18,3,1,0,0,0,19,
        20,5,2,0,0,20,21,5,4,0,0,21,22,5,3,0,0,22,23,5,5,0,0,23,5,1,0,0,
        0,24,25,5,1,0,0,25,26,5,2,0,0,26,27,5,5,0,0,27,7,1,0,0,0,2,11,17
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "<INVALID>", "<INVALID>", "'='", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "PRINT", "ID", "CADENA", "IGUAL", "PC", 
                      "WS" ]

    RULE_root = 0
    RULE_sentencia = 1
    RULE_asignacion = 2
    RULE_impresion = 3

    ruleNames =  [ "root", "sentencia", "asignacion", "impresion" ]

    EOF = Token.EOF
    PRINT=1
    ID=2
    CADENA=3
    IGUAL=4
    PC=5
    WS=6

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
            return self.getToken(ExprParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(ExprParser.SentenciaContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_root




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.sentencia()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==2):
                    break

            self.state = 13
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(ExprParser.AsignacionContext,0)


        def impresion(self):
            return self.getTypedRuleContext(ExprParser.ImpresionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_sentencia




    def sentencia(self):

        localctx = ExprParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.asignacion()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.impresion()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def IGUAL(self):
            return self.getToken(ExprParser.IGUAL, 0)

        def CADENA(self):
            return self.getToken(ExprParser.CADENA, 0)

        def PC(self):
            return self.getToken(ExprParser.PC, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_asignacion




    def asignacion(self):

        localctx = ExprParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(ExprParser.ID)
            self.state = 20
            self.match(ExprParser.IGUAL)
            self.state = 21
            self.match(ExprParser.CADENA)
            self.state = 22
            self.match(ExprParser.PC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(ExprParser.PRINT, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def PC(self):
            return self.getToken(ExprParser.PC, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_impresion




    def impresion(self):

        localctx = ExprParser.ImpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_impresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(ExprParser.PRINT)
            self.state = 25
            self.match(ExprParser.ID)
            self.state = 26
            self.match(ExprParser.PC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





