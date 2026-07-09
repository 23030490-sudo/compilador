import streamlit as st
from antlr4 import *
from Expr3Lexer import Expr3Lexer

# Número de control: 23030490

st.title("Analizador Léxico - Ejercicio 12 POO (Java)")

opcion = st.radio("¿Cómo quieres ingresar el código?", ["Escribir texto", "Subir archivo"])

codigo = None

if opcion == "Escribir texto":
    codigo = st.text_area("Escribe tu código Java aquí:", height=250)
else:
    archivo = st.file_uploader("Sube tu archivo .txt", type=["txt"])
    if archivo is not None:
        codigo = archivo.read().decode("utf-8")

if codigo and st.button("Analizar"):
    input_stream = InputStream(codigo)
    lexer = Expr3Lexer(input_stream)
    tokens = CommonTokenStream(lexer)
    tokens.fill()

    st.subheader("Tokens encontrados")

    for token in tokens.tokens:
        if token.type == Token.EOF:
            nombre = "EOF"
        else:
            nombre = lexer.symbolicNames[token.type]

        st.write(
            f"**Texto:** `{token.text}` | "
            f"**Tipo:** {nombre} | "
            f"**Línea:** {token.line} | "
            f"**Columna:** {token.column}"
        )