"""
Tarea 03/03/2023:
- Indicar el penúltimo elemento de la lista, si existe.
- Indicar los elementos entre dos posiciones (inicial y final, siendo inicial < final) de la lista.
- Eliminar todas las apariciones de un dato en la lista.
- Indicar si dos listas son iguales en longitud y contenido (elementos-orden).
- Mover un elemento desde una posición inicial, a una posición final de la lista.
"""

class NodoSimple:
    def __init__(self, dato) -> None:
        self.dato = dato
        self.siguiente = None

    def __str__(self) -> str:
        return self.dato
    

class ListaEnlazadaSimple:
    # Constructor
    def __init__(self) -> None:
        self.nodoInicial = None

    # Verificar si está vacía
    def estaVacia(self) -> bool:
        return self.nodoInicial == None

    # Adicionarl al inicio
    def adicionarAlInicio(self, dato_nuevo) -> None:
        nodoNuevo = NodoSimple(dato_nuevo)
        if self.estaVacia():
            self.nodoInicial = nodoNuevo
        else:
            nodoNuevo.siguiente = self.nodoInicial
            self.nodoInicial = nodoNuevo

    # Eliminar al inicio
    def eliminarAlInicio(self) -> (int | float | str | None):
        if self.estaVacia():
            return None
        else:
            dato = self.nodoInicial.dato
            self.nodoInicial = self.nodoInicial.siguiente
            return dato

    # Buscar un dato
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
    
    # Imprimir datos
    def __str__(self) -> str:
        recorrido = ""
        nodoActual = self.nodoInicial
        while nodoActual != None:
            recorrido = recorrido + str(nodoActual.dato) + " "
            nodoActual = nodoActual.siguiente
        return recorrido
    
    # Eliminar dato (primer encontrado)
    def eliminarDato(self, dato_eliminar) -> bool:
        if self.estaVacia():
            return False
        
        if self.nodoInicial.dato == dato_eliminar:
            self.eliminarAlInicio()
            return True

        nodoPrevio = None
        nodoActual = self.nodoInicial
        while nodoActual != None and nodoActual.dato != dato_eliminar:
            nodoPrevio = nodoActual
            nodoActual = nodoActual.siguiente
        
        if nodoActual == None:
            return False
        
        if nodoActual.siguiente == None:
            nodoPrevio.siguiente = None
        else:
            nodoPrevio.siguiente = nodoActual.siguiente
        return True

    # Adicionar al final
    def adicionarAlFinal(self, dato_nuevo) -> None:
        nodoNuevo = NodoSimple(dato_nuevo)
        if self.estaVacia():
            self.nodoInicial = nodoNuevo
        else:
            nodoActual = self.nodoInicial
            while nodoActual.siguiente != None:
                nodoActual = nodoActual.siguiente
            nodoActual.siguiente = nodoNuevo
    
    # Eliminar al final
    def eliminarAlFinal(self) -> (int | float | str | None):
        if self.estaVacia():
            return None
        else:
            nodoPrevio = None
            nodoActual = self.nodoInicial
            while nodoActual.siguiente != None:
                nodoPrevio = nodoActual
                nodoActual = nodoActual.siguiente
            nodoPrevio.siguiente = None
            return nodoActual.dato

    # Repeticiones de un dato
    def repeticionesDato(self, dato_buscar) -> (int | None):
        if self.estaVacia():
            return None
        else:
            cont = 0
            nodoActual = self.nodoInicial
            while nodoActual != None:
                if nodoActual.dato == dato_buscar:
                    cont = cont + 1
                nodoActual = nodoActual.siguiente
            return cont

    # Elemento en posición dada
    def elementoEnPosicion(self, posicion) -> (int | float | str | None):
        if self.estaVacia() or posicion < 0:
            return None

        nodaActual = self.nodoInicial
        cont = 0
        while nodaActual != None and cont < posicion:
            nodaActual = nodaActual.siguiente
            cont = cont + 1

        if nodaActual is None:
            return None
        else:
            return nodaActual.dato

    # Último elemento   
    def ultimoElemento(self) -> (int | float | str | None):
        if self.estaVacia():
            return None

        if self.nodoInicial.siguiente == None:
            return self.nodoInicial.dato
        
        nodoActual = self.nodoInicial
        while nodoActual.siguiente != None:
            nodoActual = nodoActual.siguiente
        return nodoActual.dato

    # Eliminar en posición dada   
    def eliminarEnPosicion(self, posicion) -> (bool | None):
        if self.estaVacia() or posicion < 0 or posicion >= self.contarNodos():
            return None

        if posicion == 0:
            self.eliminarAlInicio()
            return True
        
        nodoPrevio = None
        nodoActual = self.nodoInicial
        cont = 0
        while nodoActual.siguiente != None and cont < posicion:
            nodoPrevio = nodoActual
            nodoActual = nodoActual.siguiente
            cont = cont + 1
        
        nodoPrevio.siguiente = nodoActual.siguiente
        return True
    
    # Extra: Cantidad de nodos
    def contarNodos(self) -> (int | None):
        if self.estaVacia():
            return None
        
        cont = 0
        nodoActual = self.nodoInicial
        while nodoActual != None:
            nodoActual = nodoActual.siguiente
            cont = cont + 1

        return cont
    
    # Extra: Obtener nodo en posición ingresada
    def obtenerNodo(self, posicion):
        if self.estaVacia():
            return None
            
        if posicion < 0 or posicion >= self.contarNodos():
            return None
        
        nodoActual = self.nodoInicial
        cont = 0
        while nodoActual != None and cont < posicion:
            nodoActual = nodoActual.siguiente
            cont += 1
        
        return nodoActual

    # 1. Penúltimo elemento
    def penultimoElemento(self):
        if self.estaVacia():
            return None
        
        if self.nodoInicial.siguiente == None:
            return None
        
        nodoPrevio = None
        nodoActual = self.nodoInicial
        while nodoActual.siguiente != None:
            nodoPrevio = nodoActual
            nodoActual = nodoActual.siguiente
        
        return nodoPrevio.dato
    
    # 2. Elemento entre dos posiciones
    def elementosEntrePosiciones(self, posInicial, posFinal):
        if self.estaVacia() or posInicial >= posFinal:
            return None
        
        nodoActual = self.nodoInicial
        cont = 0
        while nodoActual.siguiente != None and cont < posInicial:
            nodoActual = nodoActual.siguiente
            cont = cont + 1

        elementos = []
        while nodoActual.siguiente != None and cont <= posFinal:
            elementos.append(nodoActual.dato)
            nodoActual = nodoActual.siguiente
            cont = cont + 1

        return elementos

    # 3. Eliminar apariciones de un dato
    def eliminarAparicionesDato(self, dato_buscar):
        if self.estaVacia():
            return None
        
        while self.nodoInicial.dato == dato_buscar:
            self.nodoInicial = self.nodoInicial.siguiente
            if self.nodoInicial is None:
                return True

        cont = 0
        nodoPrevio = None
        nodoActual = self.nodoInicial
        while nodoActual != None:
            if nodoActual.dato == dato_buscar:
                nodoPrevio.siguiente = nodoActual.siguiente
            else:
                nodoPrevio = nodoActual
            nodoActual = nodoActual.siguiente
        
        return True
    
    # 5. Mover elemento de posición inicial a posicón final
    def moverElemento(self, posInicial, posFinal):
        if self.estaVacia():
            return None
    
        if posInicial < 0 or posFinal < 0:
            return None
        
        if posInicial >= self.contarNodos() or posFinal >= self.contarNodos():
            return None
        
        if posInicial == posFinal:
            return None
        
        pass


# Clase comparadora de listas simples
class ComparadoraListasSimples:
    def __init__(self, lista1: ListaEnlazadaSimple, lista2: ListaEnlazadaSimple) -> None:
        self.listaSimple1 = lista1
        self.listaSimple2 = lista2

    # 4. Indicar si dos listas son iguales (longitud y contenido)
    def compararLongitud(self) -> bool:
        longitud_lista1 = self.listaSimple1.contarNodos()
        longitud_lista2 = self.listaSimple2.contarNodos()
        if longitud_lista1 == longitud_lista2:
            return True
        else:
            return False
        
    def compararContenido(self) -> bool:
        contenido_lista1 = self.listaSimple1.__str__()
        contenido_lista2 = self.listaSimple2.__str__()
        if contenido_lista1 == contenido_lista2:
            return True
        else:
            return False
        
    def compararLongitudContenido(self) -> bool:
        if self.compararLongitud() and self.compararContenido():
            return True
        else:
            return False


# Creación lista
miLista = ListaEnlazadaSimple()
miLista.adicionarAlFinal(10)
miLista.adicionarAlFinal(20)
miLista.adicionarAlFinal(30)
miLista.adicionarAlFinal(40)
miLista.adicionarAlFinal(50)
print(f"-> Lista: {miLista} ({miLista.contarNodos()} nodos)")

# 1. Penúltimo elemento
print(f"Penúltimo elemento: {miLista.penultimoElemento()}")

# 2. Elementos entre dos posiciones
print(f"Elementos entre posicón 0 y 4: {miLista.elementosEntrePosiciones(0, 4)}")
print(f"Elementos entre posicón 0 y 3: {miLista.elementosEntrePosiciones(0, 3)}")
print(f"Elementos entre posicón 0 y 2: {miLista.elementosEntrePosiciones(0, 2)}")
print(f"Elementos entre posicón 0 y 1: {miLista.elementosEntrePosiciones(0, 1)}")
print(f"Elementos entre posicón 0 y 0: {miLista.elementosEntrePosiciones(0, 0)}")

# 3. Eliminar todas las aparaciones dato
miLista.adicionarAlFinal(10)
miLista.adicionarAlFinal(20)
miLista.adicionarAlFinal(30)
miLista.adicionarAlFinal(40)
miLista.adicionarAlFinal(50)
print(f"-> Lista: {miLista} ({miLista.contarNodos()} nodos)")
print(f"Eliminar todos los 50: {miLista.eliminarAparicionesDato(50)}")
print(f"-> Lista: {miLista} ({miLista.contarNodos()} nodos)")

# 4. Indicar si dos listas son iguales (longitud y contenido)
lista1 = ListaEnlazadaSimple()
lista1.adicionarAlFinal(10)
lista1.adicionarAlFinal(20)
lista1.adicionarAlFinal(30)

lista2 = ListaEnlazadaSimple()
lista2.adicionarAlFinal(10)
lista2.adicionarAlFinal(20)
lista2.adicionarAlFinal(30)

comparacion1 = ComparadoraListasSimples(lista1, lista2)

print(f"-> Lista1: {lista1}")
print(f"-> Lista2: {lista2}")
print(f"¿Son del mismo tamaño?: {comparacion1.compararLongitud()}")
print(f"¿Tienen mismo contenido?: {comparacion1.compararContenido()}")
print(f"¿Tienen mismo tamaño Y contenido?: {comparacion1.compararContenido()}")

# 5. Mover elemento de posición inicial a posicón final
# miLista.eliminarAlFinal()
# miLista.eliminarAlFinal()
# miLista.eliminarAlFinal()
# miLista.eliminarAlFinal()

# print(f"-> Lista: {miLista} ({miLista.contarNodos()} nodos)")
# print(f"Mover posición 0 a 1: {miLista.moverElemento(0, 1)}")
# print(f"-> Lista: {miLista} ({miLista.contarNodos()} nodos)")
