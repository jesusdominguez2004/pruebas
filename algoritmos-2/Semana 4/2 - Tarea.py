"""
Tarea 17/02/2023:
- Adicionar un elemento al final de la lista.
- Eliminar el último de la lista.
- Indicar el número de apariciones de un dato en la lista.
- Indicar el elemento en una posición indicada de la lista, si existe.
- Indicar el último elemento de la lista.
- Eliminar una posición indicada de la lista, si existe.
"""

class NodoSimple:
    def __init__(self, dato) -> None:
        self.dato = dato
        self.siguiente = None

    def __str__(self) -> str:
        return self.dato
    

class ListaEnlazadaSimple:
    def __init__(self) -> None:
        self.nodoInicial = None

    def estaVacia(self) -> bool:
        return self.nodoInicial == None

    def adicionarAlInicio(self, dato_nuevo) -> None:
        nodoNuevo = NodoSimple(dato_nuevo)
        if self.estaVacia():
            self.nodoInicial = nodoNuevo
        else:
            nodoNuevo.siguiente = self.nodoInicial
            self.nodoInicial = nodoNuevo

    def eliminarAlInicio(self) -> (int | float | str | None):
        if self.estaVacia():
            return None
        else:
            dato = self.nodoInicial.dato
            self.nodoInicial = self.nodoInicial.siguiente
            return dato

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
    
    def __str__(self) -> str:
        recorrido = ""
        nodoActual = self.nodoInicial
        while nodoActual != None:
            recorrido = recorrido + str(nodoActual.dato) + " "
            nodoActual = nodoActual.siguiente
        return recorrido
    
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

    # 1. Adicionar al final
    def adicionarAlFinal(self, dato_nuevo) -> None:
        nodoNuevo = NodoSimple(dato_nuevo)
        if self.estaVacia():
            self.nodoInicial = nodoNuevo
        else:
            nodoActual = self.nodoInicial
            while nodoActual.siguiente != None:
                nodoActual = nodoActual.siguiente
            nodoActual.siguiente = nodoNuevo
    
    # 2. Eliminar al final
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

    # 3. Repeticiones de un dato
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

    # 4. Elemento en posición dada
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

    # 5. Último elemento   
    def ultimoElemento(self) -> (int | float | str | None):
        if self.estaVacia():
            return None

        if self.nodoInicial.siguiente == None:
            return self.nodoInicial.dato
        
        nodoActual = self.nodoInicial
        while nodoActual.siguiente != None:
            nodoActual = nodoActual.siguiente
        return nodoActual.dato

    # 6. Eliminar en posición dada   
    def eliminarEnPosicion(self, posicion) -> (int | float | str | None):
        if self.estaVacia() or posicion < 0:
            return None

        if posicion == 0:
            self.eliminarAlInicio()
            return True
        
        cont = 0
        nodoActual = self.nodoInicial
        while nodoActual.siguiente != None:
            nodoActual = nodoActual.siguiente
            cont = cont + 1

        if posicion > cont:
            return None
        
        return True



# 1. Adicionar al final
miLista = ListaEnlazadaSimple()
miLista.adicionarAlFinal(10)
miLista.adicionarAlFinal(20)
miLista.adicionarAlFinal(30)
print(f"-> Lista: {miLista}")

# 2. Eliminar al final
miLista.eliminarAlFinal()
print(f"-> Último nodo eliminado: {miLista}")

# 3. Repeticiones de un dato
print(f"Repeticiones de 10: {miLista.repeticionesDato(10)}")
print(f"Repeticiones de 20: {miLista.repeticionesDato(20)}")
print(f"Repeticiones de 30: {miLista.repeticionesDato(30)}")

# 4. Elemento en posición dada
miLista.adicionarAlFinal(30)
print(f"-> Lista: {miLista}")
print(f"Elemento en la posición {-3}: {miLista.elementoEnPosicion(-3)}")
print(f"Elemento en la posición {-2}: {miLista.elementoEnPosicion(-2)}")
print(f"Elemento en la posición {-1}: {miLista.elementoEnPosicion(-1)}")
print(f"Elemento en la posición {0}: {miLista.elementoEnPosicion(0)}")
print(f"Elemento en la posición {1}: {miLista.elementoEnPosicion(1)}")
print(f"Elemento en la posición {2}: {miLista.elementoEnPosicion(2)}")
print(f"Elemento en la posición {3}: {miLista.elementoEnPosicion(3)}")

# 5. Último elemento
miLista.adicionarAlFinal(40)
miLista.adicionarAlFinal(50)
print(f"-> Lista: {miLista}")
print(f"Último elemento: {miLista.ultimoElemento()}")

# 6. Eliminar en posición dada
print(f"Eliminar elemento en posición {0}: {miLista.eliminarEnPosicion(0)}")
print(f"-> Lista: {miLista}")