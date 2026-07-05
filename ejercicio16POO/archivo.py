#Número de control: 22031091

import os


class Archivo:

    def __init__(self, ruta):
        self.ruta = ruta

    def existe(self):
        return os.path.exists(self.ruta)

    def extension(self):
        return os.path.splitext(self.ruta)[1]

    def es_el_tipo_correcto(self):
        return self.extension() == ".js"

    def leer(self):
        with open(self.ruta, "r", encoding="utf-8") as archivo:
            return archivo.read()

    def imprimir_info(self):
        print("\nINFORMACION DEL ARCHIVO")
        print("-" * 40)
        print("Ruta:", self.ruta)
        print("Extension:", self.extension())