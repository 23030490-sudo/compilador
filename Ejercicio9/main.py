from antlr4 import *
from ExprLexer import ExprLexer

# Número de control: 23030149

modo = input("¿Leer desde archivo o terminal? (a = archivo, t = terminal): ")

if modo == "a":
    nombre_archivo = input("Nombre del archivo (ej: entrada.txt): ")
    input_stream = FileStream(nombre_archivo, encoding='utf-8')
else:
    texto = input("? ")
    input_stream = InputStream(texto)

lexer = ExprLexer(input_stream)
tokens = CommonTokenStream(lexer)
tokens.fill()

for token in tokens.tokens:
    print("Texto:", token.text)
    print("Tipo número:", token.type)

    if token.type == Token.EOF:
        print("Nombre token: EOF")
    else:
        print("Nombre token:", lexer.symbolicNames[token.type])

    print("Línea:", token.line)
    print("Columna:", token.column)
    print("Inicio:", token.start)
    print("Fin:", token.stop)
    print("Índice:", token.tokenIndex)
    print("Canal:", token.channel)
    print("------------------")