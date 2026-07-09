from antlr4 import *
from ExprLexer import ExprLexer;
from ExprParser import ExprParser

entrada = input("Código: ")
lexer = ExprLexer(InputStream(entrada))
tokens = CommonTokenStream(lexer)
parser = ExprParser(tokens)
arbol = parser.root()

if parser.getNumberOfSyntaxErrors() == 0 :
    print("El código es correcto")
    print("Árbol sintáctico:")
    print(arbol.toStringTree(recog=parser))
else:
    print("El código tiene errores de sintaxis")
