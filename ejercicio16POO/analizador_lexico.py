#Número de control: 22031091

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from Expr16Lexer import Expr16Lexer


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
        self.errores = ErroresLexicos()

        entrada = InputStream(codigo)
        self.lexer = Expr16Lexer(entrada)

        self.lexer.removeErrorListeners()
        self.lexer.addErrorListener(self.errores)

        self.tokens = CommonTokenStream(self.lexer)
        self.tokens.fill()

    def imprimir_tokens(self):
        print("\nTOKENS ENCONTRADOS")
        print("-" * 80)
        print(f"{'LEXEMA':<25} {'TOKEN':<25} {'TIPO':<8} {'LINEA':<8} {'COLUMNA':<8}")
        print("-" * 80)

        for token in self.tokens.tokens:

            if token.type == Token.EOF:
                continue

            nombre = self.lexer.symbolicNames[token.type]

            print(f"{token.text:<25} {nombre:<25} {token.type:<8} {token.line:<8} {token.column:<8}")

    def obtener_errores_personalizados(self):
        errores_personalizados = []

        for token in self.tokens.tokens:

            if token.type == Token.EOF:
                continue

            nombre = self.lexer.symbolicNames[token.type]

            if nombre == "IDENTIFICADOR_INVALIDO":
                errores_personalizados.append(
                    f"Linea {token.line}, columna {token.column}: "
                    f"Identificador invalido '{token.text}'. "
                    f"Un identificador en JavaScript no debe iniciar con numero."
                )

        return errores_personalizados

    def imprimir_errores(self):
        print("\nERRORES LEXICOS")
        print("-" * 40)

        errores_personalizados = self.obtener_errores_personalizados()

        if len(self.errores.lista) == 0 and len(errores_personalizados) == 0:
            print("No hay errores lexicos")

        else:
            for error in self.errores.lista:
                print(f"Linea {error[0]}, columna {error[1]}: {error[2]}")

            for error in errores_personalizados:
                print(error)