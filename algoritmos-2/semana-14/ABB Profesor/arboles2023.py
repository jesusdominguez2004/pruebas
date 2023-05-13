#Clase Arbol Binario General
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

#Clase Arbol Binario de Búsqueda (ABB)
class ArbolBinarioBusqueda:
    def __init__(self) -> None:
        self.raiz = None
    
    def estaVacio(self) -> bool:
        return self.raiz == None
    
    def __str__(self) -> str:
        if not self.estaVacio():
            return self.raiz.verArbol()
        return ""
    
    def __repr__(self) -> str:
        return self.__str__()
    
    #Recorrido
    def enOrden(self):
        if not self.estaVacio():
            return self.raiz.enOrden()
        return None

    #Insercion
    def insertar(self, elemento):
        if self.estaVacio():
            self.raiz = ArbolBinario(elemento)
        self.__insertar(self.raiz, elemento)

    def __insertar(self, arbol:ArbolBinario, elemento):
        if elemento == arbol.valor_nodo:
            return
        if elemento < arbol.valor_nodo:
            if arbol.hijo_izquierdo is None:
                arbol.hijo_izquierdo = ArbolBinario(elemento)
            else:
                self.__insertar(arbol.hijo_izquierdo, elemento)
        else:
            if arbol.hijo_derecho is None:
                arbol.hijo_derecho = ArbolBinario(elemento)
            else:
                self.__insertar(arbol.hijo_derecho, elemento)
    
    #Búsqueda
    def buscar(self, elemento) -> ArbolBinario:
        if not self.estaVacio():
            return self.__buscar(self.raiz, elemento)
        return None
    
    def __buscar(self, arbol:ArbolBinario, elemento):
        if elemento == arbol.valor_nodo:
            return arbol
        if elemento < arbol.valor_nodo:
            if arbol.hijo_izquierdo is not None:
                return self.__buscar(arbol.hijo_izquierdo, elemento)
            else:
                return None
        else:
            if arbol.hijo_derecho is not None:
                return self.__buscar(arbol.hijo_derecho, elemento)
            else:
                return None
    #Eliminar
    def eliminar(self, elemento):
        if not self.estaVacio():
            return self.__eliminar(self.raiz, elemento, None)
        return False
    
    def __eliminar(self, arbol:ArbolBinario, elemento, padre:ArbolBinario):
        if arbol is None:
            return False
        if elemento < arbol.valor_nodo:
            return self.__eliminar(arbol.hijo_izquierdo, elemento, arbol)
        elif elemento > arbol.valor_nodo:
            return self.__eliminar(arbol.hijo_derecho, elemento, arbol)
        else:
            #Caso Nodo hoja
            if arbol.esHoja():
                #Caso Nodo Hoja y Raiz
                if arbol == self.raiz:
                    self.raiz = None
                    return True
                #Actualizacion enlace nodo padre
                if padre.hijo_izquierdo == arbol:
                    padre.hijo_izquierdo = None
                else:
                    padre.hijo_derecho = None
                return True
            #Caso Nodo con un hijo
            if arbol.hijo_izquierdo is None and arbol.hijo_derecho is not None:
                #Nodo con hijo derecho únicamente
                #Caso Raiz
                if arbol == self.raiz:
                    self.raiz = arbol.hijo_derecho
                    return True
                #Actualizacion enlace nodo padre ("padre.hijo_izquierdo is not None" es por una excepción en Java...)
                if padre.hijo_izquierdo is not None and padre.hijo_izquierdo == arbol:
                    padre.hijo_izquierdo = arbol.hijo_derecho
                else:
                    padre.hijo_derecho = arbol.hijo_derecho
                return True
            if arbol.hijo_izquierdo is not None and arbol.hijo_derecho is None:
                #Nodo con hijo izquierdo únicamente
                #Caso Raiz
                if arbol == self.raiz:
                    self.raiz = arbol.hijo_izquierdo
                    return True
                #Actualizacion enlace nodo padre
                if padre.hijo_izquierdo is not None and padre.hijo_izquierdo == arbol:
                    padre.hijo_izquierdo = arbol.hijo_izquierdo
                else:
                    padre.hijo_derecho = arbol.hijo_izquierdo
                return True
            #Caso Nodo interno (tiene dos hijos)
            nodo_izquierdo:ArbolBinario = arbol.hijo_izquierdo
            nodo_temporal:ArbolBinario = None            
            while nodo_izquierdo.hijo_derecho is not None:
                nodo_temporal = nodo_izquierdo
                nodo_izquierdo = nodo_izquierdo.hijo_derecho
            arbol.valor_nodo = nodo_izquierdo.valor_nodo
            if nodo_temporal is None:
                arbol.hijo_izquierdo = nodo_izquierdo.hijo_izquierdo
            elif nodo_temporal.hijo_izquierdo == nodo_izquierdo:
                nodo_temporal.hijo_izquierdo = nodo_izquierdo.hijo_izquierdo
            elif nodo_temporal.hijo_derecho == nodo_izquierdo:
                nodo_temporal.hijo_derecho = nodo_izquierdo.hijo_izquierdo
            return True