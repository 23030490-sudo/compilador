from antlr import *

from ExprLexer import ExprLexer

#Lo que obtiene es la entrada, analiza el texto y lo separa en tokens
lexer = ExprLexer(InpurStream(input("? ")))

tokens = CommonTokenStream(lexer)
tokens.fill()

print(tokens)