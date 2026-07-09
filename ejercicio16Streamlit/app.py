#Número de control: 22031091

import streamlit as st
import pandas as pd
from analizador_lexico import AnalizadorLexico


class Ejercicio16Streamlit:

    def __init__(self):
        self.analizador = AnalizadorLexico()

    def configurar_pagina(self):
        st.set_page_config(
            page_title="Ejercicio 16: JavaScript",
            page_icon="🟨",
            layout="wide"
        )

    def mostrar_encabezado(self):
        st.title("Ejercicio 16: JavaScript")
        st.write("Nivel: Junior Medio")
        st.write("Programación: Streamlit")
        st.write("Este analizador identifica tokens básicos de JavaScript y detecta identificadores inválidos.")

    def obtener_entrada_archivo(self):
        archivo = st.file_uploader(
            "Sube un archivo de entrada (.js)",
            type=["js"]
        )

        if archivo is not None:
            contenido = archivo.read().decode("utf-8")
            st.success("Archivo JS cargado correctamente")
            return contenido

        return ""

    def obtener_entrada_manual(self):
        codigo = st.text_area(
            "Escribe código JavaScript directamente:",
            height=200,
            placeholder="Ejemplo: let 2numero = 10;"
        )

        return codigo

    def analizar_codigo(self, codigo):
        if codigo.strip() == "":
            st.warning("Primero ingresa código o sube un archivo.")
            return

        self.analizador.analizar(codigo)

        st.subheader("Entrada original")
        st.code(codigo, language="javascript")

        tokens = self.analizador.obtener_tokens()
        errores = self.analizador.obtener_errores()

        st.subheader("Tokens encontrados")

        if len(tokens) > 0:
            tabla = pd.DataFrame(tokens)
            st.dataframe(tabla, use_container_width=True)
        else:
            st.info("No se encontraron tokens.")

        st.subheader("Errores léxicos")

        if len(errores) == 0:
            st.success("No hay errores léxicos")
        else:
            for error in errores:
                st.error(
                    f"Línea {error['linea']}, columna {error['columna']}: {error['mensaje']}"
                )

    def ejecutar(self):
        self.configurar_pagina()
        self.mostrar_encabezado()

        opcion = st.radio(
            "Selecciona el tipo de entrada:",
            ["Entrada por archivo JS", "Entrada directa"]
        )

        codigo = ""

        if opcion == "Entrada por archivo JS":
            codigo = self.obtener_entrada_archivo()

        elif opcion == "Entrada directa":
            codigo = self.obtener_entrada_manual()

        if st.button("Analizar"):
            self.analizar_codigo(codigo)


class Main:

    def __init__(self):
        self.app = Ejercicio16Streamlit()

    def iniciar(self):
        self.app.ejecutar()


if __name__ == "__main__":
    main = Main()
    main.iniciar()