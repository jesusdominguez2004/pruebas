# Árboles | Crear nodos | Semana 12

class Nodos:
    def __init__(self, x) -> None:
        self.dato = x
        self.izquierda = None
        self.derecha = None

    def __str__(self) -> str:
        return str(self.dato)

nodo01 = Nodos(0)
nodo02 = Nodos(1)
nodo03 = Nodos(2)

# Ramas para nodo01
nodo01.izquierda = nodo02
nodo01.derecha = nodo03


print(nodo01)

print(nodo01.izquierda, nodo01.derecha) # Sí tiene ramas
print(nodo02.izquierda, nodo02.derecha) # No tiene ramas
print(nodo03.izquierda, nodo03.derecha) # No tiene ramas
