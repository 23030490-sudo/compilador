#Número de control: 22031091

from archivo import Archivo
from analizador_lexico import AnalizadorLexico

class Ejercicio16POO:

    def __init__(self):
        self.analizador = AnalizadorLexico()

    def mostrar_menu(self):
        print("EJERCICIO 16: JAVASCRIPT")
        print("¿Cómo deseas ingresar el código?")
        print("1. Leer desde un archivo (.js)")
        print("2. Escribir directamente en la consola/terminal")

    def leer_desde_archivo(self):
        ruta = input("Escribe la ruta del archivo: ").strip()
        archivo = Archivo(ruta)

        if not archivo.existe():
            print("El archivo no existe")
            return None

        if not archivo.es_el_tipo_correcto():
            print("El archivo debe ser .js")
            return None

        archivo.imprimir_info()
        return archivo.leer()

    def leer_desde_terminal(self):
        print("\nEscribe el código JavaScript a analizar:")
        print("Nota: para este modo se recomienda escribir una sola línea.")
        codigo = input("? ")
        return codigo

    def analizar_codigo(self, codigo):
        print("\nENTRADA ORIGINAL")
        print("-" * 40)
        print(codigo)

        self.analizador.analizar(codigo)
        self.analizador.imprimir_tokens()
        self.analizador.imprimir_errores()

    def ejecutar(self):
        self.mostrar_menu()

        opcion = input("Selecciona una opción (1 o 2): ").strip()

        if opcion == "1":
            codigo = self.leer_desde_archivo()

            if codigo is not None:
                self.analizar_codigo(codigo)

        elif opcion == "2":
            codigo = self.leer_desde_terminal()
            self.analizar_codigo(codigo)

        else:
            print("Opción no válida")


class Main:

    def __init__(self):
        self.ejercicio = Ejercicio16POO()

    def iniciar(self):
        self.ejercicio.ejecutar()


if __name__ == "__main__":
    app = Main()
    app.iniciar()