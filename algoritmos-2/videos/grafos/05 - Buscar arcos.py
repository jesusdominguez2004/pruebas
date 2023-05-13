# Clase grafo

class Arco:
    def __init__(self, verticeInical, verticeFinal, peso: int) -> None:
        self.verticeInicial = verticeInical
        self.verticeFinal = verticeFinal
        self.peso = peso

    def __repr__(self) -> str:
        return f"[{self.verticeInicial}, {self.verticeFinal}]: {self.peso}"

    def __str__(self) -> str:
        return self.__repr__()
    
    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, Arco):
            return False
        return self.verticeInicial == otro.verticeInicial and \
                self.verticeFinal == otro.verticeFinal and \
                self.peso == otro.peso
    
    def __hash__(self) -> int:
        return hash(str(self))
    

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

    def verVertices(self):
        return list(self.__listaVertices.keys())
    
    def contarVertices(self):
        return len(self.__listaVertices)
    
    def existenAmbosVertices(self, verticeInicial, verticeFinal):
        buscarIninial = self.buscarVertice(verticeInicial)
        buscarFinal = self.buscarVertice(verticeFinal)
        if buscarIninial is None or buscarFinal is None:
            return False
        else:
            return True
        
    def adicionarArco(self, verticeInicial, verticeFinal, peso: int = 0):
        if self.existenAmbosVertices(verticeInicial, verticeFinal):
            arco = Arco(verticeInicial, verticeFinal, peso)
            conjunto: set = self.buscarVertice(verticeInicial)
            conjunto.add(arco)

    def buscarArcoConPeso(self, verticeInicial, verticeFinal, peso: int):
        if self.existenAmbosVertices(verticeInicial, verticeFinal):
            arcoTemporal = Arco(verticeInicial, verticeFinal, peso)
            return arcoTemporal in self.buscarVertice(verticeInicial)
    
    def buscarArcoSinPeso(self, verticeInicial, verticeFinal):
        if self.existenAmbosVertices(verticeInicial, verticeFinal):
            conjunto: set = self.buscarVertice(verticeInicial)
            arco: Arco
            for arco in conjunto:
                if verticeFinal == arco.verticeFinal:
                    return True

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

print(lista_01.verVertices(), type(lista_01.verVertices()))
print(lista_01.contarVertices())

print(lista_01.existenAmbosVertices("A", "C"))
print(lista_01.existenAmbosVertices("A", "B"))
print(lista_01.existenAmbosVertices("A", "D"))

lista_01.adicionarArco("A", "B")
lista_01.adicionarArco("A", "C")
lista_01.adicionarArco("B", "C")

print(lista_01)

print(lista_01.buscarArcoConPeso("A", "B", 0))
print(lista_01.buscarArcoConPeso("A", "B", 2))
print(lista_01.buscarArcoSinPeso("A", "B"))

