#Clase Grafo
class GrafoLista:
    def __init__(self) -> None:
        self.__lista_vertices = dict()
    
    def __str__(self) -> str:
        return str(self.__lista_vertices)
    
    def buscarVertice(self, dato_buscar):
        return self.__lista_vertices.get(dato_buscar)
    
    def adicionarVertice(self, dato_nuevo_vertice):
        if self.buscarVertice(dato_nuevo_vertice) is None:
            lista_adyacentes = set()
            self.__lista_vertices[dato_nuevo_vertice] = lista_adyacentes
    
    def verVertices(self):
        return list(self.__lista_vertices.keys())
    
    def adicionarArco(self, vertice_inicial, vertice_final):
        busqueda_inicial = self.buscarVertice(vertice_inicial)
        busqueda_final = self.buscarVertice(vertice_final)
        if busqueda_inicial is None or busqueda_final is None:
            return False
        busqueda_inicial.add(vertice_final)
    
    def sonAdyacentes(self, vertice_inicial, vertice_final):
        busqueda_inicial = self.buscarVertice(vertice_inicial)
        busqueda_final = self.buscarVertice(vertice_final)
        if busqueda_inicial is None or busqueda_final is None:
            return False
        return vertice_final in busqueda_inicial   
    
    #RECORRIDOS
    #RECORRIDO EN PROFUNDIDAD DFS
    def __dfs(self, list_recorrido:list, set_visitados:set, vertice_actual):
        list_recorrido.append(vertice_actual)
        set_visitados.add(vertice_actual)
        adyacentes_actual = self.buscarVertice(vertice_actual)
        for ady_actual in adyacentes_actual:
            if ady_actual not in set_visitados:
                list_recorrido, set_visitados = self.__dfs(list_recorrido, set_visitados, ady_actual)
        return list_recorrido, set_visitados

    def recorrerProfundidad(self, vertice_inicial):        
        if self.buscarVertice(vertice_inicial) is None:
            return None        
        recorrido, visitados = self.__dfs(list(), set(), vertice_inicial)
        for vertice in self.verVertices():
            if vertice not in visitados:
                recorrido, visitados = self.__dfs(recorrido, visitados, vertice)
        return recorrido
    
    #RECORRIDO EN ANCHURA BFS    
    def __bfs(self, list_recorrido:list, set_visitados:set, vertice_actual):
        list_recorrido.append(vertice_actual)
        set_visitados.add(vertice_actual)
        cola_ady = [vertice_actual]
        while cola_ady:
            vertice_cola = cola_ady.pop(0)        
            adyacentes_actual_cola = self.buscarVertice(vertice_cola)
            for ady_actual in adyacentes_actual_cola:
                if ady_actual not in set_visitados:
                    list_recorrido.append(ady_actual)
                    set_visitados.add(ady_actual)
                    cola_ady.append(ady_actual)
        return list_recorrido, set_visitados

    def recorrerAnchura(self, vertice_inicial):
        if self.buscarVertice(vertice_inicial) is None:
            return None        
        recorrido, visitados = self.__bfs(list(), set(), vertice_inicial)
        for vertice in self.verVertices():
            if vertice not in visitados:
                recorrido, visitados = self.__bfs(recorrido, visitados, vertice)
        return recorrido