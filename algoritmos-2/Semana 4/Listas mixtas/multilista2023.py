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

#Clase Nodo Doble
class NodoDoble(NodoSimple):
    #Constructor
    def __init__(self, dato):
        super().__init__(dato)
        self.secundario = None
    #Eq
    def __eq__(self, other):
        if not isinstance(other, NodoDoble):
            return False
        return self.dato == other.dato
#Clase Multilista
class Multilista:
    def __init__(self) -> None:
        self.nodoInicial = None
        self.nodoFinal = None
    
    #Lista Vacia
    def estaVacia(self):
        return self.nodoInicial == None
    
    #Contar la cantidad de elementos
    def longitud(self):
        nodoActual = self.nodoInicial
        contador = 0
        while nodoActual != None:
            contador += 1
            nodoActual = nodoActual.siguiente
        return contador
    
    #Str
    def __str__(self):
        recorrido = ""
        nodoActual = self.nodoInicial
        while nodoActual != None:
            recorrido += str(nodoActual.dato) + " "
            nodoActual = nodoActual.siguiente
        return recorrido

    #Gestion Lista Principal
    #Agregar dato principal
    def adicionarPrincipal(self, dato_nuevo):
        nodoNuevo = NodoDoble(dato_nuevo)
        if self.estaVacia():
            self.nodoInicial = self.nodoFinal = nodoNuevo
        else:
            nodoActual = self.nodoFinal            
            nodoActual.siguiente = nodoNuevo            
            self.nodoFinal = nodoNuevo
    #Buscar dato principal
    def buscarPrincipal(self, dato_buscar):
        if self.estaVacia():
            return False
        else:
            nodoActual = self.nodoInicial
            while nodoActual != None:
                if nodoActual.dato == dato_buscar:
                    return True
                nodoActual = nodoActual.siguiente
            return False

    #Gestion Lista Secundaria
    #Agregar dato secundaria
    def adicionarSecundaria(self, dato_buscar, dato_nuevo):
        if self.estaVacia():
            return False
        else:
            nodoPrincipal = self.nodoInicial
            while nodoPrincipal != None and nodoPrincipal.dato != dato_buscar:
                nodoPrincipal = nodoPrincipal.siguiente
            if nodoPrincipal != None:
                #Ubicado nodo principal
                nodoNuevo = NodoSimple(dato_nuevo)
                if nodoPrincipal.secundario == None: #Primer nodo secundario
                    nodoPrincipal.secundario = nodoNuevo
                else:
                    nodoBusqueda = nodoPrincipal.secundario
                    while nodoBusqueda.siguiente != None:
                        nodoBusqueda = nodoBusqueda.siguiente
                    nodoBusqueda.siguiente = nodoNuevo
                return True
            return False
    #Recorrer secundarios
    def verSecundaria(self, dato_buscar):
        if self.estaVacia():
            return None
        else:
            nodoPrincipal = self.nodoInicial
            while nodoPrincipal != None and nodoPrincipal.dato != dato_buscar:
                nodoPrincipal = nodoPrincipal.siguiente
            if nodoPrincipal != None:
                #Ubicado nodo principal
                nodoBusqueda = nodoPrincipal.secundario
                recorrido = ""
                while nodoBusqueda != None:
                    recorrido += str(nodoBusqueda.dato) + " "
                    nodoBusqueda = nodoBusqueda.siguiente                          
                return recorrido
            return None


