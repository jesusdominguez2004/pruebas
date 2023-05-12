#Clase Arbol (nodosBinarios)
class ArbolBinario:
    def __init__(self, dato, arbol_izquierdo = None, arbol_derecho = None) -> None:
        self.valor_nodo = dato
        self.hijo_izquierdo = arbol_izquierdo
        self.hijo_derecho = arbol_derecho     

    def esHoja(self):
        return self.hijo_izquierdo == None and self.hijo_derecho == None
    
    def __str__(self) -> str:
        return str(self.valor_nodo)
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, ArbolBinario):
            return False
        return self.valor_nodo == otro.valor_nodo

    #Visualización Arbol      
    def verArbol(self) -> str: 
        return self.__verArbol(self,"")
    
    # parámetro: "nombreClase" -> misma clase
    # parámetro: nombreClase -> otra clase
    # Python trabaja por valor, no por referecia
    # Estudiar recursividad Python (Ojo)
    def __verArbol(self, arbol:"ArbolBinario", recorrido:str, nivel = 0) -> str:
        espaciado = "\t" * nivel        
        if arbol is None:
            return ""
        recorrido =  espaciado + str(arbol.valor_nodo) + "\n" \
            + str(self.__verArbol(arbol.hijo_izquierdo, recorrido, nivel+1)) + \
            str(self.__verArbol(arbol.hijo_derecho, recorrido, nivel + 1)) + recorrido
        return recorrido        
    
    #RECORRIDOS
    #Preorden
    def preOrden(self):
        visitados = list()
        self.__preOrden(self, visitados)
        return visitados
    
    def __preOrden(self, arbol:"ArbolBinario", visitados:list):
        if arbol is not None:
            visitados.append(arbol)
            visitados = self.__preOrden(arbol.hijo_izquierdo, visitados)
            visitados = self.__preOrden(arbol.hijo_derecho, visitados)
        return visitados
    #EnOrden
    def enOrden(self):
        visitados = list()
        self.__enOrden(self, visitados)
        return visitados
    
    def __enOrden(self, arbol:"ArbolBinario", visitados:list):
        if arbol is not None:
            visitados = self.__enOrden(arbol.hijo_izquierdo, visitados)
            visitados.append(arbol)
            visitados = self.__enOrden(arbol.hijo_derecho, visitados)
        return visitados
    #PosOrden
    def posOrden(self):
        visitados = list()
        self.__posOrden(self, visitados)
        return visitados
    
    def __posOrden(self, arbol:"ArbolBinario", visitados:list):
        if arbol is not None:
            visitados = self.__posOrden(arbol.hijo_izquierdo, visitados)
            visitados = self.__posOrden(arbol.hijo_derecho, visitados)
            visitados.append(arbol)
        return visitados

