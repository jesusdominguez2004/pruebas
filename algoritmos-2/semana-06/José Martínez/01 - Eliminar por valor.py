# Eliminar nodos por valor

class NodoSimple:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaSimple:
    def __init__(self):
        self.nodoInicial = None

    def __str__(self) -> str:
        cadena = ""
        actual = self.nodoInicial
        while actual is not None:
            cadena = cadena + str(actual.dato) + " "
            actual = actual.siguiente
        return cadena
    
    def adicionarAlFinal(self, nodoNuevo: NodoSimple):
        if self.nodoInicial is None:
            self.nodoInicial = nodoNuevo
        else:
            actual = self.nodoInicial
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nodoNuevo

    # MÉTODO RÚBRICA
    def eliminarPorValor(self, valor_buscar):
        if self.nodoInicial is None:
            return "Lista vacía..."
        
        if self.nodoInicial.dato == valor_buscar:
            self.nodoInicial = self.nodoInicial.siguiente
            return True
        
        previo = None
        actual = self.nodoInicial
        while actual.siguiente != None and actual.dato != valor_buscar:
            previo = actual
            actual = actual.siguiente

        if actual == None:
            return False
        
        if actual.siguiente == None:
            previo.siguiente = None
        else:
            previo.siguiente = actual.siguiente
        
        return True

# Intanciar lista enlazada simple
lista = ListaSimple()

# Crear y añadir nodos simples
nodo_1 = NodoSimple("A")
nodo_2 = NodoSimple("B")
nodo_3 = NodoSimple("C")
nodo_4 = NodoSimple("D")
nodo_5 = NodoSimple("E")

lista.adicionarAlFinal(nodo_1)
lista.adicionarAlFinal(nodo_2)
lista.adicionarAlFinal(nodo_3)
lista.adicionarAlFinal(nodo_4)
lista.adicionarAlFinal(nodo_5)

# Imprimir lista simple con __str__
print("Lista simple:", lista)

# Eliminar por valor
print("Eliminar 'A':", lista.eliminarPorValor("A"))
print("Lista simple:", lista)

print("Eliminar 'E':", lista.eliminarPorValor("E"))
print("Lista simple:", lista)

print("Eliminar 'C':", lista.eliminarPorValor("C"))
print("Lista simple:", lista)
