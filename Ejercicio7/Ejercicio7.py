from antlr4 import *
from ExprLexer import ExprLexer
from antlr4.Token import Token

def analizar(texto):
    lexer = ExprLexer(InputStream(texto))
    tokens = CommonTokenStream(lexer)
    tokens.fill()

    print("LEXEMA\t\tTOKEN")
    print("-------------------------")

    for token in tokens.tokens:
        if token.type == Token.EOF:
            continue

        nombre_token = lexer.symbolicNames[token.type]
        print(f"{token.text}\t\t{nombre_token}")


print("1. Entrada desde terminal")
print("2. Entrada desde archivo")
opcion = input("Selecciona una opción: ")

if opcion == "1":
    texto = input("Ingresa la entrada: ")
    analizar(texto)

elif opcion == "2":
    with open("entrada.txt", "r", encoding="utf-8") as archivo:
        texto = archivo.read()
    analizar(texto)

else:
    print("Opción no válida")