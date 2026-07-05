#Número de control: 22031091
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from Expr15Lexer import Expr15Lexer


class ErroresLexicos(ErrorListener):

    def __init__(self):
        self.lista = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.lista.append({
            "linea": line,
            "columna": column,
            "mensaje": msg
        })


class AnalizadorLexico:

    def __init__(self):
        self.lexer = None
        self.tokens = None
        self.errores = ErroresLexicos()

    def analizar(self, codigo):
        self.errores = ErroresLexicos()

        entrada = InputStream(codigo)
        self.lexer = Expr15Lexer(entrada)

        self.lexer.removeErrorListeners()
        self.lexer.addErrorListener(self.errores)

        self.tokens = CommonTokenStream(self.lexer)
        self.tokens.fill()

    def obtener_tokens(self):
        lista_tokens = []

        for token in self.tokens.tokens:

            if token.type == Token.EOF:
                continue

            nombre = self.lexer.symbolicNames[token.type]

            lista_tokens.append({
                "Lexema": token.text,
                "Token": nombre,
                "Tipo": token.type,
                "Línea": token.line,
                "Columna": token.column
            })

        return lista_tokens

    def obtener_errores(self):
        return self.errores.lista