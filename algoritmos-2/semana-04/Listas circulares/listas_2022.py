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
    
    #Str
    def __str__(self):
        recorrido = ""
        nodoActual = self.nodoInicial
        while nodoActual != None:
            recorrido += str(nodoActual.dato) + " "
            nodoActual = nodoActual.siguiente
        return recorrido

    #Buscar por posición
    def buscarPosicion(self, posicion):
        if self.estaVacia():
            return None
        if posicion < 0:
            raise Exception("La posición debe ser mayor o igual a cero!")
        nodoActual = self.nodoInicial
        contador_posicion = 0
        while (nodoActual != None and contador_posicion < posicion):
            contador_posicion += 1
            nodoActual = nodoActual.siguiente
        if nodoActual == None:
            return None
        return nodoActual.dato

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

    #Contar la cantidad de elementos
    def longitud(self):
        nodoActual = self.nodoInicial
        contador = 0
        while nodoActual != None:
            contador += 1
            nodoActual = nodoActual.siguiente
        return contador
#Diseño Lista Doble
#Clase Nodo Doble
class NodoDoble(NodoSimple):
    #Constructor
    def __init__(self, dato):
        super().__init__(dato)
        self.previo = None
    #Eq
    def __eq__(self, other):
        if not isinstance(other, NodoDoble):
            return False
        return self.dato == other.dato
# Clase ListaDoble
class ListaDoble(ListaSimple):
    # Constructor
    def __init__(self) -> None:
        super().__init__()        

    # Adicionar al inicio
    def adicionarAlInicio(self, dato_nuevo):
        nodoNuevo = NodoDoble(dato_nuevo)
        if self.estaVacia():
            self.nodoInicial = nodoNuevo
        else:
            nodoNuevo.siguiente = self.nodoInicial
            self.nodoInicial.previo = nodoNuevo
            self.nodoInicial = nodoNuevo

    #Adicionar al final
    def adicionarAlFinal(self, dato_nuevo):
        nodoNuevo = NodoDoble(dato_nuevo)
        if self.estaVacia():
            self.nodoInicial = nodoNuevo
        else:
            nodoActual = self.nodoInicial
            while (nodoActual.siguiente != None):
                nodoActual = nodoActual.siguiente
            nodoActual.siguiente = nodoNuevo
            nodoNuevo.previo = nodoActual

    #Eliminar al inicio
    def eliminarAlInicio(self):
        if self.estaVacia():
            return None
        else:
            dato = self.nodoInicial.dato
            self.nodoInicial = self.nodoInicial.siguiente
            if self.nodoInicial != None:
                self.nodoInicial.previo = None
            return dato

    # Eliminar por información
    def eliminarInfo(self, dato_eliminar):
        if self.estaVacia():
            return False
        if self.nodoInicial.dato == dato_eliminar:
            self.eliminarAlInicio()
            return True
        nodoActual = self.nodoInicial
        while nodoActual != None and nodoActual.dato != dato_eliminar:
            nodoActual = nodoActual.siguiente
        if nodoActual == None:
            return False
        nodoPrevio = nodoActual.previo
        if nodoActual.siguiente == None:
            nodoPrevio.siguiente = None
        else:
            nodoPrevio.siguiente = nodoActual.siguiente
            nodoSiguiente = nodoActual.siguiente
            nodoSiguiente.previo = nodoPrevio
        return True
#Diseño Lista Circular
# Clase ListaCircularDoble
class ListaCircular(ListaDoble):
    # Constructor
    def __init__(self) -> None:
        super().__init__()        

    # Adicionar al inicio
    def adicionarAlInicio(self, dato_nuevo):
        nodoNuevo = NodoDoble(dato_nuevo)
        if self.estaVacia():
            self.nodoInicial = nodoNuevo
            #Conexion circular
            nodoNuevo.siguiente = nodoNuevo.previo = nodoNuevo
        else:
            nodoFinal = self.nodoInicial.previo
            nodoNuevo.siguiente = self.nodoInicial
            self.nodoInicial.previo = nodoNuevo
            self.nodoInicial = nodoNuevo
            #Conexion circular
            nodoFinal.siguiente = self.nodoInicial
            self.nodoInicial.previo = nodoFinal
    #Adicionar al final
    def adicionarAlFinal(self, dato_nuevo):
        nodoNuevo = NodoDoble(dato_nuevo)
        if self.estaVacia():
            self.nodoInicial = nodoNuevo
            #Conexion circular
            nodoNuevo.siguiente = nodoNuevo.previo = nodoNuevo
        else:
            nodoFinal = self.nodoInicial.previo           
            nodoFinal.siguiente = nodoNuevo
            nodoNuevo.previo = nodoFinal
            nodoFinal = nodoNuevo
            #Conexion circular
            nodoFinal.siguiente = self.nodoInicial
            self.nodoInicial.previo = nodoFinal

    #Eliminar al inicio
    def eliminarAlInicio(self):
        if self.estaVacia():
            return None
        else:
            nodoFinal = self.nodoInicial.previo
            dato = self.nodoInicial.dato
            if self.nodoInicial.siguiente == self.nodoInicial:
                self.nodoInicial = None
                return dato
            self.nodoInicial = self.nodoInicial.siguiente
            if self.nodoInicial != None:
                self.nodoInicial.previo = nodoFinal
                nodoFinal.siguiente = self.nodoInicial
            return dato

    # Eliminar por información
    def eliminarInfo(self, dato_eliminar):
        if self.estaVacia():
            return False
        if self.nodoInicial.dato == dato_eliminar:
            self.eliminarAlInicio()
            return True
        nodoActual = self.nodoInicial
        nodoFinal = nodoActual.previo
        while nodoActual != nodoFinal and nodoActual.dato != dato_eliminar:
            nodoActual = nodoActual.siguiente
        if nodoActual.dato != dato_eliminar:
            return False
        nodoPrevio = nodoActual.previo
        if nodoActual.siguiente == self.nodoInicial:
            nodoPrevio.siguiente = self.nodoInicial
            nodoFinal = nodoPrevio
            self.nodoInicial.previo = nodoFinal
        else:
            nodoPrevio.siguiente = nodoActual.siguiente
            nodoSiguiente = nodoActual.siguiente
            nodoSiguiente.previo = nodoPrevio
        return True
    
    #Sobreescritura str
    def __str__(self):
        if self.estaVacia():
            return ""
        if self.nodoInicial == self.nodoInicial.siguiente:
            return str(self.nodoInicial.dato)        
        nodoActual = self.nodoInicial
        recorrido = str(nodoActual.dato) + " "
        nodoActual = nodoActual.siguiente
        while nodoActual != self.nodoInicial:
            recorrido += str(nodoActual.dato) + " "
            nodoActual = nodoActual.siguiente
        return recorrido