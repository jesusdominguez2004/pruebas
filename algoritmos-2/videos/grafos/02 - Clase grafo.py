# Clase grafo

class ListaAdyacencia:
    def __init__(self) -> None:
        self.__listaVertices = dict()
    
    def __str__(self) -> str:
        return str(self.__listaVertices)

    def buscarVertice(self, datoBuscar):
        return self.__listaVertices.get(datoBuscar)
    
    def adicionarVertice(self, nuevoVertice):
        if self.buscarVertice(nuevoVertice) is None:
            listaAdyacentes = set()
            self.__listaVertices[nuevoVertice] = listaAdyacentes



lista_01 = ListaAdyacencia()
print(lista_01)

lista_01.adicionarVertice("A")
lista_01.adicionarVertice("B")
lista_01.adicionarVertice("C")
print(lista_01)

print(lista_01.buscarVertice("A"))
print(lista_01.buscarVertice("B"))
print(lista_01.buscarVertice("C"))
print(lista_01.buscarVertice("D"))

