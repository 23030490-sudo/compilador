from antlr4 import *
from ExprLexer import ExprLexer
from antlr4.Token import Token

lexer = ExprLexer(InputStream(input("? ")))

tokens = CommonTokenStream(lexer)
tokens.fill()

for token in tokens.tokens:
    if token.type == Token.EOF:
        continue

    print("Texto:", token.text)
    print("Tipo:", lexer.symbolicNames[token.type])
    print("--------------------")