# Generated from Expr15.g4 by ANTLR 4.13.2
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
        4,1,20,117,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,
        0,10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,1,2,3,2,22,8,2,1,2,1,2,5,2,26,
        8,2,10,2,12,2,29,9,2,1,2,5,2,32,8,2,10,2,12,2,35,9,2,1,2,1,2,5,2,
        39,8,2,10,2,12,2,42,9,2,1,2,3,2,45,8,2,1,2,1,2,5,2,49,8,2,10,2,12,
        2,52,9,2,1,2,5,2,55,8,2,10,2,12,2,58,9,2,1,2,1,2,5,2,62,8,2,10,2,
        12,2,65,9,2,1,2,5,2,68,8,2,10,2,12,2,71,9,2,1,2,1,2,5,2,75,8,2,10,
        2,12,2,78,9,2,1,2,1,2,5,2,82,8,2,10,2,12,2,85,9,2,1,2,5,2,88,8,2,
        10,2,12,2,91,9,2,1,2,1,2,1,2,5,2,96,8,2,10,2,12,2,99,9,2,1,2,3,2,
        102,8,2,1,2,1,2,5,2,106,8,2,10,2,12,2,109,9,2,3,2,111,8,2,1,3,1,
        3,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,2,1,0,10,11,1,0,12,18,134,0,13,1,
        0,0,0,2,18,1,0,0,0,4,110,1,0,0,0,6,112,1,0,0,0,8,114,1,0,0,0,10,
        12,3,2,1,0,11,10,1,0,0,0,12,15,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,
        0,14,16,1,0,0,0,15,13,1,0,0,0,16,17,5,0,0,1,17,1,1,0,0,0,18,19,3,
        4,2,0,19,3,1,0,0,0,20,22,5,1,0,0,21,20,1,0,0,0,21,22,1,0,0,0,22,
        23,1,0,0,0,23,27,5,2,0,0,24,26,3,6,3,0,25,24,1,0,0,0,26,29,1,0,0,
        0,27,25,1,0,0,0,27,28,1,0,0,0,28,33,1,0,0,0,29,27,1,0,0,0,30,32,
        3,8,4,0,31,30,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,
        34,111,1,0,0,0,35,33,1,0,0,0,36,40,5,3,0,0,37,39,3,6,3,0,38,37,1,
        0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,111,1,0,0,0,42,
        40,1,0,0,0,43,45,5,1,0,0,44,43,1,0,0,0,44,45,1,0,0,0,45,46,1,0,0,
        0,46,50,5,4,0,0,47,49,3,6,3,0,48,47,1,0,0,0,49,52,1,0,0,0,50,48,
        1,0,0,0,50,51,1,0,0,0,51,56,1,0,0,0,52,50,1,0,0,0,53,55,3,8,4,0,
        54,53,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,111,1,
        0,0,0,58,56,1,0,0,0,59,63,5,5,0,0,60,62,3,6,3,0,61,60,1,0,0,0,62,
        65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,69,1,0,0,0,65,63,1,0,0,
        0,66,68,3,8,4,0,67,66,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,
        1,0,0,0,70,111,1,0,0,0,71,69,1,0,0,0,72,76,5,6,0,0,73,75,3,8,4,0,
        74,73,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,111,1,
        0,0,0,78,76,1,0,0,0,79,83,5,7,0,0,80,82,3,6,3,0,81,80,1,0,0,0,82,
        85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,89,1,0,0,0,85,83,1,0,0,
        0,86,88,3,8,4,0,87,86,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,
        1,0,0,0,90,111,1,0,0,0,91,89,1,0,0,0,92,93,5,8,0,0,93,97,5,16,0,
        0,94,96,3,8,4,0,95,94,1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,97,98,
        1,0,0,0,98,111,1,0,0,0,99,97,1,0,0,0,100,102,5,1,0,0,101,100,1,0,
        0,0,101,102,1,0,0,0,102,103,1,0,0,0,103,107,5,9,0,0,104,106,3,8,
        4,0,105,104,1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,
        0,0,108,111,1,0,0,0,109,107,1,0,0,0,110,21,1,0,0,0,110,36,1,0,0,
        0,110,44,1,0,0,0,110,59,1,0,0,0,110,72,1,0,0,0,110,79,1,0,0,0,110,
        92,1,0,0,0,110,101,1,0,0,0,111,5,1,0,0,0,112,113,7,0,0,0,113,7,1,
        0,0,0,114,115,7,1,0,0,115,9,1,0,0,0,17,13,21,27,33,40,44,50,56,63,
        69,76,83,89,97,101,107,110
    ]

class Expr15Parser ( Parser ):

    grammarFileName = "Expr15.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'sudo'", "'nmap'", "'ss'", "'tcpdump'", 
                     "'curl'", "'dig'", "'journalctl'", "'grep'", "'ufw'" ]

    symbolicNames = [ "<INVALID>", "SUDO", "NMAP", "SS", "TCPDUMP", "CURL", 
                      "DIG", "JOURNALCTL", "GREP", "UFW", "OPCION_CORTA", 
                      "OPCION_LARGA", "RANGO_IP", "IP", "RUTA", "DOMINIO", 
                      "CADENA", "PALABRA", "NUMERO", "COMENTARIO_LINEA", 
                      "WS" ]

    RULE_root = 0
    RULE_linea = 1
    RULE_comando = 2
    RULE_opcion = 3
    RULE_valor = 4

    ruleNames =  [ "root", "linea", "comando", "opcion", "valor" ]

    EOF = Token.EOF
    SUDO=1
    NMAP=2
    SS=3
    TCPDUMP=4
    CURL=5
    DIG=6
    JOURNALCTL=7
    GREP=8
    UFW=9
    OPCION_CORTA=10
    OPCION_LARGA=11
    RANGO_IP=12
    IP=13
    RUTA=14
    DOMINIO=15
    CADENA=16
    PALABRA=17
    NUMERO=18
    COMENTARIO_LINEA=19
    WS=20

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
            return self.getToken(Expr15Parser.EOF, 0)

        def linea(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Expr15Parser.LineaContext)
            else:
                return self.getTypedRuleContext(Expr15Parser.LineaContext,i)


        def getRuleIndex(self):
            return Expr15Parser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)




    def root(self):

        localctx = Expr15Parser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1022) != 0):
                self.state = 10
                self.linea()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(Expr15Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comando(self):
            return self.getTypedRuleContext(Expr15Parser.ComandoContext,0)


        def getRuleIndex(self):
            return Expr15Parser.RULE_linea

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLinea" ):
                listener.enterLinea(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLinea" ):
                listener.exitLinea(self)




    def linea(self):

        localctx = Expr15Parser.LineaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_linea)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.comando()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NMAP(self):
            return self.getToken(Expr15Parser.NMAP, 0)

        def SUDO(self):
            return self.getToken(Expr15Parser.SUDO, 0)

        def opcion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Expr15Parser.OpcionContext)
            else:
                return self.getTypedRuleContext(Expr15Parser.OpcionContext,i)


        def valor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Expr15Parser.ValorContext)
            else:
                return self.getTypedRuleContext(Expr15Parser.ValorContext,i)


        def SS(self):
            return self.getToken(Expr15Parser.SS, 0)

        def TCPDUMP(self):
            return self.getToken(Expr15Parser.TCPDUMP, 0)

        def CURL(self):
            return self.getToken(Expr15Parser.CURL, 0)

        def DIG(self):
            return self.getToken(Expr15Parser.DIG, 0)

        def JOURNALCTL(self):
            return self.getToken(Expr15Parser.JOURNALCTL, 0)

        def GREP(self):
            return self.getToken(Expr15Parser.GREP, 0)

        def CADENA(self):
            return self.getToken(Expr15Parser.CADENA, 0)

        def UFW(self):
            return self.getToken(Expr15Parser.UFW, 0)

        def getRuleIndex(self):
            return Expr15Parser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)




    def comando(self):

        localctx = Expr15Parser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_comando)
        self._la = 0 # Token type
        try:
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 20
                    self.match(Expr15Parser.SUDO)


                self.state = 23
                self.match(Expr15Parser.NMAP)
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10 or _la==11:
                    self.state = 24
                    self.opcion()
                    self.state = 29
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 520192) != 0):
                    self.state = 30
                    self.valor()
                    self.state = 35
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.match(Expr15Parser.SS)
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10 or _la==11:
                    self.state = 37
                    self.opcion()
                    self.state = 42
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 43
                    self.match(Expr15Parser.SUDO)


                self.state = 46
                self.match(Expr15Parser.TCPDUMP)
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10 or _la==11:
                    self.state = 47
                    self.opcion()
                    self.state = 52
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 520192) != 0):
                    self.state = 53
                    self.valor()
                    self.state = 58
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 59
                self.match(Expr15Parser.CURL)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10 or _la==11:
                    self.state = 60
                    self.opcion()
                    self.state = 65
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 520192) != 0):
                    self.state = 66
                    self.valor()
                    self.state = 71
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 72
                self.match(Expr15Parser.DIG)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 520192) != 0):
                    self.state = 73
                    self.valor()
                    self.state = 78
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 79
                self.match(Expr15Parser.JOURNALCTL)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10 or _la==11:
                    self.state = 80
                    self.opcion()
                    self.state = 85
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 520192) != 0):
                    self.state = 86
                    self.valor()
                    self.state = 91
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 92
                self.match(Expr15Parser.GREP)
                self.state = 93
                self.match(Expr15Parser.CADENA)
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 520192) != 0):
                    self.state = 94
                    self.valor()
                    self.state = 99
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 100
                    self.match(Expr15Parser.SUDO)


                self.state = 103
                self.match(Expr15Parser.UFW)
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 520192) != 0):
                    self.state = 104
                    self.valor()
                    self.state = 109
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpcionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPCION_CORTA(self):
            return self.getToken(Expr15Parser.OPCION_CORTA, 0)

        def OPCION_LARGA(self):
            return self.getToken(Expr15Parser.OPCION_LARGA, 0)

        def getRuleIndex(self):
            return Expr15Parser.RULE_opcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpcion" ):
                listener.enterOpcion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpcion" ):
                listener.exitOpcion(self)




    def opcion(self):

        localctx = Expr15Parser.OpcionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_opcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            _la = self._input.LA(1)
            if not(_la==10 or _la==11):
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


    class ValorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RANGO_IP(self):
            return self.getToken(Expr15Parser.RANGO_IP, 0)

        def IP(self):
            return self.getToken(Expr15Parser.IP, 0)

        def RUTA(self):
            return self.getToken(Expr15Parser.RUTA, 0)

        def DOMINIO(self):
            return self.getToken(Expr15Parser.DOMINIO, 0)

        def CADENA(self):
            return self.getToken(Expr15Parser.CADENA, 0)

        def PALABRA(self):
            return self.getToken(Expr15Parser.PALABRA, 0)

        def NUMERO(self):
            return self.getToken(Expr15Parser.NUMERO, 0)

        def getRuleIndex(self):
            return Expr15Parser.RULE_valor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValor" ):
                listener.enterValor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValor" ):
                listener.exitValor(self)




    def valor(self):

        localctx = Expr15Parser.ValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_valor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 520192) != 0)):
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





