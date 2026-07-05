#Número de control: 22031091

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from Expr15Lexer import Expr15Lexer

class ErroresLexicos(ErrorListener):

    def __init__(self):
        self.lista = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.lista.append([line, column, msg])

class AnalizadorLexico:

    def __init__(self):
        self.lexer = None
        self.tokens = None
        self.errores = ErroresLexicos()

    def analizar(self, codigo):
        entrada = InputStream(codigo)
        self.lexer = Expr15Lexer(entrada)

        self.lexer.removeErrorListeners()
        self.lexer.addErrorListener(self.errores)

        self.tokens = CommonTokenStream(self.lexer)
        self.tokens.fill()

    def imprimir_tokens(self):
        print("\nTOKENS ENCONTRADOS")
        print("-" * 80)
        print(f"{'LEXEMA':<25} {'TOKEN':<20} {'TIPO':<8} {'LINEA':<8} {'COLUMNA':<8}")
        print("-" * 80)

        for token in self.tokens.tokens:
            if token.type == Token.EOF:
                continue

            nombre = self.lexer.symbolicNames[token.type]
            print(f"{token.text:<25} {nombre:<20} {token.type:<8} {token.line:<8} {token.column:<8}")

    def imprimir_errores(self):
        print("\nERRORES LEXICOS")
        print("-" * 40)

        if len(self.errores.lista) == 0:
            print("No hay errores lexicos")
        else:
            for error in self.errores.lista:
                print(f"Linea {error[0]}, columna {error[1]}: {error[2]}")