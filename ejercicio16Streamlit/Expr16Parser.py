# Generated from Expr16.g4 by ANTLR 4.13.2
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
        4,1,13,39,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,3,1,21,8,1,1,2,1,2,1,2,1,2,1,2,
        1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,0,0,5,0,2,4,6,8,
        0,1,1,0,9,11,35,0,13,1,0,0,0,2,20,1,0,0,0,4,22,1,0,0,0,6,28,1,0,
        0,0,8,36,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,15,1,0,0,0,13,11,
        1,0,0,0,13,14,1,0,0,0,14,16,1,0,0,0,15,13,1,0,0,0,16,17,5,0,0,1,
        17,1,1,0,0,0,18,21,3,4,2,0,19,21,3,6,3,0,20,18,1,0,0,0,20,19,1,0,
        0,0,21,3,1,0,0,0,22,23,5,1,0,0,23,24,5,10,0,0,24,25,5,4,0,0,25,26,
        3,8,4,0,26,27,5,6,0,0,27,5,1,0,0,0,28,29,5,2,0,0,29,30,5,5,0,0,30,
        31,5,3,0,0,31,32,5,7,0,0,32,33,3,8,4,0,33,34,5,8,0,0,34,35,5,6,0,
        0,35,7,1,0,0,0,36,37,7,0,0,0,37,9,1,0,0,0,2,13,20
    ]

class Expr16Parser ( Parser ):

    grammarFileName = "Expr16.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'let'", "'console'", "'log'", "'='", 
                     "'.'", "';'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "LET", "CONSOLE", "LOG", "IGUAL", "PUNTO", 
                      "PUNTO_COMA", "PARENTESIS_ABRE", "PARENTESIS_CIERRA", 
                      "IDENTIFICADOR_INVALIDO", "ID", "NUMERO", "COMENTARIO_LINEA", 
                      "WS" ]

    RULE_root = 0
    RULE_sentencia = 1
    RULE_declaracion = 2
    RULE_impresion = 3
    RULE_valor = 4

    ruleNames =  [ "root", "sentencia", "declaracion", "impresion", "valor" ]

    EOF = Token.EOF
    LET=1
    CONSOLE=2
    LOG=3
    IGUAL=4
    PUNTO=5
    PUNTO_COMA=6
    PARENTESIS_ABRE=7
    PARENTESIS_CIERRA=8
    IDENTIFICADOR_INVALIDO=9
    ID=10
    NUMERO=11
    COMENTARIO_LINEA=12
    WS=13

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
            return self.getToken(Expr16Parser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Expr16Parser.SentenciaContext)
            else:
                return self.getTypedRuleContext(Expr16Parser.SentenciaContext,i)


        def getRuleIndex(self):
            return Expr16Parser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)




    def root(self):

        localctx = Expr16Parser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 10
                self.sentencia()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(Expr16Parser.EOF)
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

        def declaracion(self):
            return self.getTypedRuleContext(Expr16Parser.DeclaracionContext,0)


        def impresion(self):
            return self.getTypedRuleContext(Expr16Parser.ImpresionContext,0)


        def getRuleIndex(self):
            return Expr16Parser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)




    def sentencia(self):

        localctx = Expr16Parser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.declaracion()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
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


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(Expr16Parser.LET, 0)

        def ID(self):
            return self.getToken(Expr16Parser.ID, 0)

        def IGUAL(self):
            return self.getToken(Expr16Parser.IGUAL, 0)

        def valor(self):
            return self.getTypedRuleContext(Expr16Parser.ValorContext,0)


        def PUNTO_COMA(self):
            return self.getToken(Expr16Parser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return Expr16Parser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)




    def declaracion(self):

        localctx = Expr16Parser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(Expr16Parser.LET)
            self.state = 23
            self.match(Expr16Parser.ID)
            self.state = 24
            self.match(Expr16Parser.IGUAL)
            self.state = 25
            self.valor()
            self.state = 26
            self.match(Expr16Parser.PUNTO_COMA)
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

        def CONSOLE(self):
            return self.getToken(Expr16Parser.CONSOLE, 0)

        def PUNTO(self):
            return self.getToken(Expr16Parser.PUNTO, 0)

        def LOG(self):
            return self.getToken(Expr16Parser.LOG, 0)

        def PARENTESIS_ABRE(self):
            return self.getToken(Expr16Parser.PARENTESIS_ABRE, 0)

        def valor(self):
            return self.getTypedRuleContext(Expr16Parser.ValorContext,0)


        def PARENTESIS_CIERRA(self):
            return self.getToken(Expr16Parser.PARENTESIS_CIERRA, 0)

        def PUNTO_COMA(self):
            return self.getToken(Expr16Parser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return Expr16Parser.RULE_impresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImpresion" ):
                listener.enterImpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImpresion" ):
                listener.exitImpresion(self)




    def impresion(self):

        localctx = Expr16Parser.ImpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_impresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(Expr16Parser.CONSOLE)
            self.state = 29
            self.match(Expr16Parser.PUNTO)
            self.state = 30
            self.match(Expr16Parser.LOG)
            self.state = 31
            self.match(Expr16Parser.PARENTESIS_ABRE)
            self.state = 32
            self.valor()
            self.state = 33
            self.match(Expr16Parser.PARENTESIS_CIERRA)
            self.state = 34
            self.match(Expr16Parser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Expr16Parser.ID, 0)

        def NUMERO(self):
            return self.getToken(Expr16Parser.NUMERO, 0)

        def IDENTIFICADOR_INVALIDO(self):
            return self.getToken(Expr16Parser.IDENTIFICADOR_INVALIDO, 0)

        def getRuleIndex(self):
            return Expr16Parser.RULE_valor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValor" ):
                listener.enterValor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValor" ):
                listener.exitValor(self)




    def valor(self):

        localctx = Expr16Parser.ValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_valor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0)):
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





