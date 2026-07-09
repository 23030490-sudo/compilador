from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser

modo = input("¿Leer desde archivo o terminal? (a = archivo, t = terminal): ")

if modo == "a":
    nombre_archivo = input("Nombre del archivo (ej: entrada.txt): ")
    input_stream = FileStream(nombre_archivo, encoding='utf-8')
else:
    entrada = input("Código: ")
    input_stream = InputStream(entrada)

lexer = ExprLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = ExprParser(tokens)
arbol = parser.root()

if parser.getNumberOfSyntaxErrors() == 0:
    print("El código es correcto")
    print("Árbol sintáctico:")
    print(arbol.toStringTree(recog=parser))
else:
    print("El código tiene errores de sintaxis")
