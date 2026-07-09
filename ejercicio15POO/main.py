#Número de control: 22031091

from archivo import Archivo
from analizador_lexico import AnalizadorLexico

class Main:

    def __init__(self):
        self.analizador = AnalizadorLexico()

    def ejecutar(self):
        print("EJERCICIO 15: COMANDOS NMAP")
        print("¿Cómo deseas ingresar el código?")
        print("1. Leer desde un archivo (.txt)")
        print("2. Escribir directamente en la consola/terminal")

        opcion = input("Selecciona una opción (1 o 2): ").strip()

        if opcion == "1":
            ruta = input("Escribe la ruta del archivo: ").strip()
            archivo = Archivo(ruta)

            if not archivo.existe():
                print("El archivo no existe")
                return

            if not archivo.es_el_tipo_correcto():
                print("El archivo debe ser .txt")
                return

            codigo = archivo.leer()
            archivo.imprimir_info()

            print("\nENTRADA ORIGINAL")
            print("-" * 40)
            print(codigo)

            self.analizador.analizar(codigo)
            self.analizador.imprimir_tokens()
            self.analizador.imprimir_errores()

        elif opcion == "2":
            print("\nEscribe el comando a analizar:")
            codigo = input("? ")

            print("\nENTRADA ORIGINAL")
            print("-" * 40)
            print(codigo)

            self.analizador.analizar(codigo)
            self.analizador.imprimir_tokens()
            self.analizador.imprimir_errores()

        else:
            print("Opción no válida")

if __name__ == "__main__":
    app = Main()
    app.ejecutar()