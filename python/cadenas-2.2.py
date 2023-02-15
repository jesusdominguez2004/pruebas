# Cadenas 2.2 | Jesús Alberto Domínguez Charris

"""
POO
cadena:
    invertida
    longitud
    vector
    palabras

    vocales SIN REPETIR + TILDES
    consonantes SIN REPETIR
    números SIN REPETIR
    signos de puntuación SIN REPETIR
    otros caracteres SIN REPETIR

    palabras CANTIDAD
    vocales CANTIDAD
    consonantes CANTIDAD
    números CANTIDAD
    signos de puntuación CANTIDAD
    otros caracteres CANTIDAD
    mayúsculas CANTIDAD
    minúsculas CANTIDAD
    espacios CANTIDAD

menú
guardar en txt
leer txt
funciones
time sleep
guardar json
leer json
guardar morse
leer morse
diccionario morse mejorado
"""
from time import sleep
import json


# Clase Cadenas
class Cadenas:
    # Constructor
    def __init__(self) -> None:
        self.__cadena = ""
        self.__invertir = ""
        self.__vector = []
        self.__longitud = 0
        self.__cantidad_palabras = 0
        self.__palabras = []
        self.__cantidad_vocales = 0
        self.__vocales = ["a", "e", "i", "o", "u",
                          "á", "é", "í", "ó", "ú",
                          "à", "è", "ì", "ò", "ù",
                          "ä", "ë", "ï", "ö", "ü"]
        self.__vocales_cadena = []
        self.__cantidad_consonantes = 0
        self.__consonantes = ["b", "c", "d", "f",
                              "g", "h", "j", "k",
                              "l", "m", "n", "ñ",
                              "p", "q", "r", "s",
                              "t", "v", "w", "x",
                              "y", "z"]
        self.__consonantes_cadena = []
        self.__cantidad_numeros = 0
        self.__numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.__numeros_cadena = []
        self.__cantidad_puntuacion = 0
        self.__puntuacion = ["¿", "?", "¡", "!",
                             "(", ")", "[", "]",
                             "{", "}", ".", ":",
                             ",", ";"]
        self.__puntuacion_cadena = []
        self.__cantidad_otros = 0
        self.__otros = ["+", "-", "*", "/", "%",
                        "<", ">", "=", "|", "°",
                        "¬", "#", "$", "&", "\\",
                        "¨", "´", "~", "^", "`",
                        "_", "@"]
        self.__otros_cadena = []
        self.__cantidad_mayusculas = 0
        self.__cantidad_minusculas = 0
        self.__cantidad_espacios = 0
        self.__diccionario = {}
        self.__cadena_morse = ""
        self.__lista_morse = []
        self.__morse_1 = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "ñ": "--.--",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.---",
            "z": "--..",
            "0": "-----",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
            " ": "/",
            "á": ".--.-",
            "é": "..-..",
            "í": "..",
            "ó": "---.",
            "ú": "..-",
            "¿": "..-.-",
            "?": "..--..",
            "¡": "--...-",
            "!": "-.-.--",
            ".": ".-.-.-",
            ":": "---...",
            ",": "--..--",
            ";": "-.-.-.",
            "(": "-.--.",
            ")": "-.--.-",
            "+": ".-.-.",
            "-": "-....-",
            "/": "-..-.",
            "=": "-...-",
            "&": ".-...",
            "@": ".--.-.",
            "$": "...-..-",
            "'": ".----.",
            "_": "..--.-"
        }
        self.__morse_2 = {
            ".-": "a",
            "-...": "b",
            "-.-.": "c",
            "-..": "d",
            ".": "e",
            "..-.": "f",
            "--.": "g",
            "....": "h",
            "..": "i",
            ".---": "j",
            "-.-": "k",
            ".-..": "l",
            "--": "m",
            "-.": "n",
            "--.--": "ñ",
            "---": "o",
            ".--.": "p",
            "--.-": "q",
            ".-.": "r",
            "...": "s",
            "-": "t",
            "..-": "u",
            "...-": "v",
            ".--": "w",
            "-..-": "x",
            "-.---": "y",
            "--..": "z",
            "-----": "0",
            ".----": "1",
            "..---": "2",
            "...--": "3",
            "....-": "4",
            ".....": "5",
            "-....": "6",
            "--...": "7",
            "---..": "8",
            "----.": "9",
            "/": " ",
            ".--.-": "á",
            "..-..": "é",
            "---.": "ó",
            "..-.-": "¿",
            "..--..": "?",
            "--...-": "¡",
            "-.-.--": "!",
            ".-.-.-": ".",
            "---...": ":",
            "--..--": ",",
            "-.-.-.": ";",
            "-.--.": "(",
            "-.--.-": ")",
            ".-.-.": "+",
            "-....-": "-",
            "-..-.": "/",
            "-...-": "=",
            ".-...": "&",
            ".--.-.": "@",
            "...-..-": "$",
            ".----.": "'",
            "..--.-": "_"
        }
        self.__contenido_txt = ""
        self.__json = ""

    # Setters and getters
    def set_cadena(self, cadena: str) -> None:
        self.__cadena = cadena

    def get_cadena(self) -> str:
        return self.__cadena

    def set_invertir(self, invertir: str) -> None:
        self.__invertir = invertir

    def get_invertir(self) -> str:
        return self.__invertir

    def set_vector(self, vector: list) -> None:
        self.__vector = vector

    def get_vector(self) -> list:
        return self.__vector

    def set_longitud(self, longitud: int) -> None:
        self.__longitud = longitud

    def get_longitud(self) -> int:
        return self.__longitud

    def set_cantidad_palabras(self, cantidad_palabras: int) -> None:
        self.__cantidad_palabras = cantidad_palabras

    def get_cantidad_palabras(self) -> int:
        return self.__cantidad_palabras

    def set_palabras(self, palabras: list) -> None:
        self.__palabras = palabras

    def get_palabras(self) -> list:
        return self.__palabras

    def set_cantidad_vocales(self, cantidad_vocales: int) -> None:
        self.__cantidad_vocales = cantidad_vocales

    def get_cantidad_vocales(self) -> int:
        return self.__cantidad_vocales

    def set_vocales(self, vocales: list) -> None:
        self.__vocales = vocales

    def get_vocales(self) -> list:
        return self.__vocales

    def set_vocales_cadena(self, vocales_cadena: list) -> None:
        self.__vocales_cadena = vocales_cadena

    def get_vocales_cadena(self) -> list:
        return self.__vocales_cadena

    def set_cantidad_consonantes(self, cantidad_consonantes: int) -> None:
        self.__cantidad_consonantes = cantidad_consonantes

    def get_cantidad_consonantes(self) -> int:
        return self.__cantidad_consonantes

    def set_consonantes(self, consonantes: list) -> None:
        self.__consonantes = consonantes

    def get_consonantes(self) -> list:
        return self.__consonantes

    def set_consonantes_cadena(self, consonantes_cadena: list) -> None:
        self.__consonantes_cadena = consonantes_cadena

    def get_consonantes_cadena(self) -> list:
        return self.__consonantes_cadena

    def set_cantidad_numeros(self, cantidad_numeros: int) -> None:
        self.__cantidad_numeros = cantidad_numeros

    def get_cantidad_numeros(self) -> int:
        return self.__cantidad_numeros

    def set_numeros(self, numeros: list) -> None:
        self.__numeros = numeros

    def get_numeros(self) -> list:
        return self.__numeros

    def set_numeros_cadena(self, numeros_cadena: list) -> None:
        self.__numeros_cadena = numeros_cadena

    def get_numeros_cadena(self) -> list:
        return self.__numeros_cadena

    def set_cantidad_puntuacion(self, cantidad_puntuacion: int) -> None:
        self.__cantidad_puntuacion = cantidad_puntuacion

    def get_cantidad_puntuacion(self) -> int:
        return self.__cantidad_puntuacion

    def set_puntuacion(self, puntuacion: list) -> None:
        self.__puntuacion = puntuacion

    def get_puntuacion(self) -> list:
        return self.__puntuacion

    def set_puntuacion_cadena(self, puntuacion_cadena: list) -> None:
        self.__puntuacion_cadena = puntuacion_cadena

    def get_puntuacion_cadena(self) -> list:
        return self.__puntuacion_cadena

    def set_cantidad_otros(self, cantidad_otros: int) -> None:
        self.__cantidad_otros = cantidad_otros

    def get_cantidad_otros(self) -> int:
        return self.__cantidad_otros

    def set_otros(self, otros: list) -> None:
        self.__otros = otros

    def get_otros(self) -> list:
        return self.__otros

    def set_otros_cadena(self, otros_cadena: list) -> None:
        self.__otros_cadena = otros_cadena

    def get_otros_cadena(self) -> list:
        return self.__otros_cadena

    def set_cantidad_mayusculas(self, cantidad_mayusculas: int) -> None:
        self.__cantidad_mayusculas = cantidad_mayusculas

    def get_cantidad_mayusculas(self) -> int:
        return self.__cantidad_mayusculas

    def set_cantidad_minusculas(self, cantidad_minusculas: int) -> None:
        self.__cantidad_minusculas = cantidad_minusculas

    def get_cantidad_minusculas(self) -> int:
        return self.__cantidad_minusculas

    def set_cantidad_espacios(self, cantidad_espacios: int) -> None:
        self.__cantidad_espacios = cantidad_espacios

    def get_cantidad_espacios(self) -> int:
        return self.__cantidad_espacios

    def set_diccionario(self, diccionario: dict) -> None:
        self.__diccionario = diccionario

    def get_diccionario(self) -> dict:
        return self.__diccionario

    def set_cadena_morse(self, cadena_morse: str) -> None:
        self.__cadena_morse = cadena_morse

    def get_cadena_morse(self) -> str:
        return self.__cadena_morse

    def set_lista_morse(self, lista_morse: list) -> None:
        self.__lista_morse = lista_morse

    def get_lista_morse(self) -> list:
        return self.__lista_morse

    def set_morse_1(self, morse_1: dict) -> None:
        self.__morse_1 = morse_1

    def get_morse_1(self) -> dict:
        return self.__morse_1

    def set_morse_2(self, morse_2: dict) -> None:
        self.__morse_2 = morse_2

    def get_morse_2(self) -> dict:
        return self.__morse_2

    def set_contenido_txt(self, contenido_txt: str) -> None:
        self.__contenido_txt = contenido_txt

    def get_contenido_txt(self) -> str:
        return self.__contenido_txt

    def set_json(self, str_json: str) -> None:
        self.__json = str_json

    def get_json(self) -> str:
        return self.__json

    # Comportamientos
    def leer_cadena(self):
        self.set_cadena(input("Ingrese su cadena: "))
        # 1. Invertir
        self.set_invertir(self.get_cadena()[::-1])
        # 2. Longitud
        self.set_longitud(len(self.get_cadena()))
        # 3. Vector
        for x in self.get_cadena():
            self.get_vector().append(x)
        # 4. Palabras
        self.set_palabras(self.get_cadena().split())
        self.set_cantidad_palabras(len(self.get_palabras()))
        # 5. Vocales
        for x in self.get_cadena():
            if x.lower() in self.get_vocales():
                self.set_cantidad_vocales(self.get_cantidad_vocales() + 1)
                if x not in self.get_vocales_cadena():
                    self.get_vocales_cadena().append(x)
        # 6. Consonantes
        for x in self.get_cadena():
            if x.lower() in self.get_consonantes():
                self.set_cantidad_consonantes(self.get_cantidad_consonantes() + 1)
                if x not in self.get_consonantes_cadena():
                    self.get_consonantes_cadena().append(x)
        # 7. Números
        for x in self.get_cadena():
            if x in self.get_numeros():
                self.set_cantidad_numeros(self.get_cantidad_numeros() + 1)
                if x not in self.get_numeros_cadena():
                    self.get_numeros_cadena().append(x)
        # 8. Signos de puntuación
        for x in self.get_cadena():
            if x.lower() in self.get_puntuacion():
                self.set_cantidad_puntuacion(self.get_cantidad_puntuacion() + 1)
                if x not in self.get_puntuacion_cadena():
                    self.get_puntuacion_cadena().append(x)
        # 9. Otros caracteres
        for x in self.get_cadena():
            if x.lower() in self.get_otros():
                self.set_cantidad_otros(self.get_cantidad_otros() + 1)
                if x not in self.get_otros_cadena():
                    self.get_otros_cadena().append(x)
        # 10. Cantidad mayúsculas y minúsculas
        for x in self.get_cadena():
            if x.isupper():
                self.set_cantidad_mayusculas(self.get_cantidad_mayusculas() + 1)
            if x.islower():
                self.set_cantidad_minusculas(self.get_cantidad_minusculas() + 1)
        # 11. Cantidad espacios
        for x in self.get_cadena():
            if x.isspace():
                self.set_cantidad_espacios(self.get_cantidad_espacios() + 1)

    def consola(self):
        print(f"Cadena: {self.get_cadena()}")
        print(f"1. Invertir: {self.get_invertir()}")
        print(f"2. Longitud: {self.get_longitud()}")
        print(f"3. Lista caracteres: {self.get_vector()}")
        print(f"4. Lista palabras: {self.get_palabras()}")
        print(f"5. Lista vocales: {self.get_vocales_cadena()}")
        print(f"6. Lista consonantes: {self.get_consonantes_cadena()}")
        print(f"7. Lista números: {self.get_numeros_cadena()}")
        print(f"8. Lista signos de puntuación: {self.get_puntuacion_cadena()}")
        print(f"9. Lista otros caracteres: {self.get_otros_cadena()}")
        print(f"10. Cantidad palabras: {self.get_cantidad_palabras()}")
        print(f"11. Cantidad vocales: {self.get_cantidad_vocales()}")
        print(f"12. Cantidad consonantes: {self.get_cantidad_consonantes()}")
        print(f"13. Cantidad números: {self.get_cantidad_numeros()}")
        print(f"14. Cantidad signos de puntuación: {self.get_cantidad_puntuacion()}")
        print(f"15. Cantidad otros caracteres: {self.get_cantidad_otros()}")
        print(f"16. Cantidad mayúsculas: {self.get_cantidad_mayusculas()}")
        print(f"17. Cantidad minúsculas: {self.get_cantidad_minusculas()}")
        print(f"18. Cantidad espacios: {self.get_cantidad_espacios()}")
        print("¡Proceso consola finalizado!\n")

    def guardar_txt(self):
        self.leer_cadena()
        with open("cadenas-2.2.txt", "w", encoding="utf-8") as file:
            file.write(f"Cadena: {self.get_cadena()}\n")
            file.write(f"1. Invertir: {self.get_invertir()}\n")
            file.write(f"2. Longitud: {self.get_longitud()}\n")
            file.write(f"3. Lista caracteres: {self.get_vector()}\n")
            file.write(f"4. Lista palabras: {self.get_palabras()}\n")
            file.write(f"5. Lista vocales: {self.get_vocales_cadena()}\n")
            file.write(f"6. Lista consonantes: {self.get_consonantes_cadena()}\n")
            file.write(f"7. Lista números: {self.get_numeros_cadena()}\n")
            file.write(f"8. Lista signos de puntuación: {self.get_puntuacion_cadena()}\n")
            file.write(f"9. Lista otros caracteres: {self.get_otros_cadena()}\n")
            file.write(f"10. Cantidad palabras: {self.get_cantidad_palabras()}\n")
            file.write(f"11. Cantidad vocales: {self.get_cantidad_vocales()}\n")
            file.write(f"12. Cantidad consonantes: {self.get_cantidad_consonantes()}\n")
            file.write(f"13. Cantidad números: {self.get_cantidad_numeros()}\n")
            file.write(f"14. Cantidad signos de puntuación: {self.get_cantidad_puntuacion()}\n")
            file.write(f"15. Cantidad otros caracteres: {self.get_cantidad_otros()}\n")
            file.write(f"16. Cantidad mayúsculas: {self.get_cantidad_mayusculas()}\n")
            file.write(f"17. Cantidad minúsculas: {self.get_cantidad_minusculas()}\n")
            file.write(f"18. Cantidad espacios: {self.get_cantidad_espacios()}")
            print("¡Proceso guardado txt finalizado!\n")

    def leer_txt(self):
        with open("cadenas-2.2.txt", "r", encoding="utf-8") as file:
            self.set_contenido_txt(file.read())
            print(self.get_contenido_txt())
            print("¡Proceso de lectura txt finalizado!\n")

    def guardar_json(self):
        self.leer_cadena()
        self.set_diccionario({
            "cadena": self.get_cadena(),
            "invertir": self.get_invertir(),
            "vector": self.get_vector(),
            "longitud": self.get_longitud(),
            "palabras": self.get_palabras(),
            "cantidad_palabras": self.get_cantidad_palabras(),
            "cantidad_vocales": self.get_cantidad_vocales(),
            "vocales_cadena": self.get_vocales_cadena(),
            "cantidad_consonantes": self.get_cantidad_consonantes(),
            "consonantes_cadena": self.get_consonantes_cadena(),
            "cantidad_numeros": self.get_cantidad_numeros(),
            "numeros_cadena": self.get_numeros_cadena(),
            "cantidad_puntuacion": self.get_cantidad_puntuacion(),
            "puntuacion_cadena": self.get_puntuacion_cadena(),
            "cantidad_otros": self.get_cantidad_otros(),
            "otros_cadena": self.get_otros_cadena(),
            "cantidad_mayusculas": self.get_cantidad_mayusculas(),
            "cantidad_minusculas": self.get_cantidad_minusculas(),
            "cantidad_espacios": self.get_cantidad_espacios()
        })
        print(type(self.get_diccionario()), self.get_diccionario())
        print(type(json.dumps(self.get_diccionario())), json.dumps(self.get_diccionario()))

        with open("json-2.2.txt", "w", encoding="utf-8") as file:
            json.dump(self.get_diccionario(), file)
        print("¡Proceso de guardado json finalizado!\n")

    def leer_json(self):
        with open("json-2.2.txt", "r", encoding="utf-8") as file:
            self.set_json(file.read())
            print(type(self.get_json()), self.get_json())

            self.set_diccionario(json.loads(self.get_json()))
            print(type(self.get_diccionario()), self.get_diccionario())
            print("¡Proceso de lectura json finalizado!\n")

    def guardar_morse(self):
        self.leer_cadena()
        for i in self.get_cadena().lower():
            self.set_cadena_morse(self.get_cadena_morse() + " " + self.get_morse_1().get(i))
        print(self.get_cadena_morse())
        with open("morse-2.2.txt", "w", encoding="utf-8") as file:
            file.write(self.get_cadena_morse())
        print("¡Proceso de guardado morse finalizado!\n")

    def leer_morse(self):
        with open("morse-2.2.txt", "r", encoding="utf-8") as file:
            self.set_cadena_morse(file.read())
            self.set_lista_morse(self.get_cadena_morse().split())
            self.set_cadena("")
            for i in self.get_lista_morse():
                self.set_cadena(self.get_cadena() + self.get_morse_2().get(i))
            print(self.get_cadena_morse())
            print(self.get_cadena())
            print("¡Proceso de lectura morse finalizado!\n")

    def menu(self):
        while True:
            print("CADENAS 2.2 | Jesús Alberto Domínguez Charris")
            print("1. Consola\n2. Guardar txt\n3. Leer txt")
            print("4. Guardar json\n5. Leer json\n6. Guardar morse")
            print("7. Leer morse\n8. Salir")
            opcion = input(">>> ")
            # Consola
            if opcion == "1":
                self.leer_cadena()
                self.consola()
            # Guardar txt
            elif opcion == "2":
                self.guardar_txt()
            # Leer txt
            elif opcion == "3":
                self.leer_txt()
            # Guardar json
            elif opcion == "4":
                self.guardar_json()
            # Leer json
            elif opcion == "5":
                self.leer_json()
            # Guardar morse
            elif opcion == "6":
                self.guardar_morse()
            # Leer morse
            elif opcion == "7":
                self.leer_morse()
            # Salir
            elif opcion == "8":
                print("¡Hasta luego!")
                break
            # Datos incorrectos
            else:
                print("Datos incorrectos...")
            # Pasua entre cada opción
            sleep(1.5)


# Método principal
def main():
    objeto_1 = Cadenas()
    objeto_1.menu()


# Llamar método principal
main()
