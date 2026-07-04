# Importa ANTLR4 para funciones
from antlr4 import*
from ExprLexer import ExprLexer

from archivo import Archivo
from analizador_lexico import AnalizadorLexico

class Main:

    def __init__(self):
        self.analizador = AnalizadorLexico()

    def ejecutar(self):
        print("¿Cómo deseas ingresar el código?")
        print("1. Leer desde un archivo (.txt)")
        print("2. Escribir directamente en la consola / terminal")
        
        opcion = input("Selecciona una opción (1 o 2): ").strip()

        if opcion == "1":
            # --- Modo Archivo ---
            ruta = input("Escribe la ruta del archivo: ")
            archivo = Archivo(ruta)

            if not archivo.existe():
                print("El archivo no existe")
                return

            if not archivo.es_el_tipo_correcto():
                print("El archivo debe ser .txt")
                return

            codigo = archivo.leer()

            archivo.imprimir_info()

            print("\nCODIGO ORIGINAL")
            print("-" * 40)
            print(codigo)

            self.analizador.analizar(codigo)
            self.analizador.imprimir_tokens()
            self.analizador.imprimir_errores()

        elif opcion == "2":
            # --- Modo Consola ---
            # Lo que obtiene es la entrada, analiza el texto y lo separa en tokens
            lexer = ExprLexer(InputStream(input("? ")))
            
            # Toma los tokens que produjo el lexer y los guarda en un flujo/lista
            tokens = CommonTokenStream(lexer)
            tokens.fill()
            
            print("\nFLUJO DE TOKENS:")
            print(tokens)
            print("-" * 40)

            for token in tokens.tokens:
                # Saltamos el token EOF (Fin de archivo) para evitar errores de índice en la lista de nombres
                if token.type == Token.EOF:
                    continue
                    
                print("Texto: ", token.text)
                print("Linea: ", token.line)
                print("Columna: ", token.column)
                
                # Obtener el nombre del token de forma segura
                nombre_token = lexer.symbolicNames[token.type]
                print("Tipo: ", nombre_token)
                print("-------------------")

        else:
            print("Opción no válida.")

# Control del punto de inicio del programa
if __name__ == "__main__":
    app = Main()
    app.ejecutar()