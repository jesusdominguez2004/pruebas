#Clase Nodo Simple
class NodoSimple:
    #Constructor
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
    #Str
    def __str__(self) -> str:
        return str(self.dato)
    #Eq
    def __eq__(self, other):
        if not isinstance(other, NodoSimple):
            return False
        return self.dato == other.dato
#Clase ListaSimple
class ListaSimple:
    #Constructor
    def __init__(self) -> None:
        self.nodoInicial = None
    
    #Lista Vacia
    def estaVacia(self):
        return self.nodoInicial == None

    #Adicionar al inicio
    def adicionarAlInicio(self, dato_nuevo):
        nodoNuevo = NodoSimple(dato_nuevo)
        if self.estaVacia():
            self.nodoInicial = nodoNuevo
        else:
            nodoNuevo.siguiente = self.nodoInicial
            self.nodoInicial = nodoNuevo
    
    #Eliminar al inicio
    def eliminarAlInicio(self):
        if self.estaVacia():
            return None
        else:
            dato = self.nodoInicial.dato
            self.nodoInicial = self.nodoInicial.siguiente
            return dato
    
    #Buscar por dato
    def buscar(self, dato_buscar):
        if self.estaVacia():
            return False
        else:
            nodoActual = self.nodoInicial
            while nodoActual != None:
                if nodoActual.dato == dato_buscar:
                    return True
                nodoActual = nodoActual.siguiente
            return False
    
    #Recorrido (Str)
    def __str__(self):
        recorrido = ""
        nodoActual = self.nodoInicial
        while nodoActual != None:
            recorrido += str(nodoActual.dato) + " "
            nodoActual = nodoActual.siguiente
        return recorrido
    
    #Eliminar por información
    def eliminarInfo(self, dato_eliminar):
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
