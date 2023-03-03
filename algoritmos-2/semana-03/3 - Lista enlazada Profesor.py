# Crear nodos simple
class NodoSimple:
    def __init__(self, dato) -> None:
        self.dato = dato
        self.siguiente = None
    
    def __str__(self) -> str:
        return str(self.dato)
    
    def __eq__(self, otro) -> bool:
        if not isinstance(otro, NodoSimple):
            return False
        return self.dato == otro.dato


# Crear lista enlazada y sus métodos
class ListaEnlazadaSimple:
    def __init__(self) -> None:
        self.nodoInicial = None
    
    # 1. Verificar lista vacía
    def estaVacia(self) -> bool:
        return self.nodoInicial == None

    # 2. Agregar al inicio
    def añadirAlInicio(self, dato_nuevo) -> None:
        nodoNuevo = NodoSimple(dato_nuevo)
        if self.estaVacia():
            self.nodoInicial = nodoNuevo
        else:
            nodoNuevo.siguiente = self.nodoInicial
            self.nodoInicial = nodoNuevo
    
    # 3. Eliminar al inicio
    def eliminarAlInicio(self):
        if self.estaVacia():
            return None
        else:
            dato = self.nodoInicial.dato
            self.nodoInicial = self.nodoInicial.siguiente
            return dato

    # 4. Buscar por datos
    def buscarDato(self, dato_buscar) -> bool:
        if self.estaVacia():
            return False
        else:
            nodoActual = self.nodoInicial
            while nodoActual != None:
                if nodoActual.dato == dato_buscar:
                    return True
                nodoActual = nodoActual.siguiente
            return False
    
    # 5. Recorrer lista
    def __str__(self) -> str:
        recorrido = ""
        nodoActual = self.nodoInicial
        while nodoActual != None:
            recorrido += str(nodoActual.dato) +  " "
            nodoActual = nodoActual.siguiente
        return recorrido

    # 6. Eliminar dato
    def eliminarDato(self, dato_eliminar) -> bool:
        # A. Cuando está vacía
        if self.estaVacia():
            return False
        # B. Cuando es el nodo inicial
        if self.nodoInicial.dato == dato_eliminar:
            self.eliminarAlInicio()
            return True
        # C. Recorrer datos
        nodoPrevio = None
        nodoActual = self.nodoInicial
        while nodoActual != None and nodoActual.dato != dato_eliminar:
            nodoPrevio = nodoActual
            nodoActual = nodoActual.siguiente
        # Si no lo encontró
        if nodoActual == None:
            return False
        # En caso de que esté en el último nodo
        if nodoActual.siguiente == None:
            nodoPrevio.siguiente = None
        # En caso de que esté entre nodos
        else:
            nodoPrevio.siguiente = nodoActual.siguiente
        return True

# Prueba 1
lista_1 = ListaEnlazadaSimple()
print(f"-> Lista 1: {lista_1}")
print(f"Vacía: {lista_1.estaVacia()}")

lista_1.añadirAlInicio(1)
lista_1.añadirAlInicio(2)
lista_1.añadirAlInicio(3)
print(f"-> Lista 1: {lista_1}")
print(f"Vacía: {lista_1.estaVacia()}")

print(f"Buscar 4: {lista_1.buscarDato(4)}")
print(f"Buscar 5: {lista_1.buscarDato(5)}")

lista_1.eliminarAlInicio()
print(f"-> Lista 1: {lista_1}\n")

# Prueba 2
lista_2 = ListaEnlazadaSimple()
lista_2.añadirAlInicio(10)
lista_2.añadirAlInicio(20)
lista_2.añadirAlInicio(30)
lista_2.añadirAlInicio(40)
lista_2.añadirAlInicio(50)
lista_2.añadirAlInicio(60)
lista_2.añadirAlInicio(70)
print(f"-> Lista 2: {lista_2}")
print(f"Eliminar 100: {lista_2.eliminarDato(100)}")
print(f"-> Lista 2: {lista_2}")
print(f"Eliminar 40: {lista_2.eliminarDato(40)}")
print(f"-> Lista 2: {lista_2}")
print(f"Eliminar 10: {lista_2.eliminarDato(10)}")
print(f"-> Lista 2: {lista_2}")
print(f"Eliminar 60: {lista_2.eliminarDato(60)}")
print(f"-> Lista 2: {lista_2}")
