class nodo:
	def __init__(self, valor):  # metodo inicializador
		self.dato      = valor
		self.siguiente = None	#   none =  Null	

class ListaEnlazada:
	def __init__(self):
		self.raiz = None  # nodo principal

	def insertarAlFinal(self, nuevo_nodo):
		if self.raiz is not None:
			ultimo_nodo = self.raiz
			while ultimo_nodo.siguiente != None:
				ultimo_nodo = ultimo_nodo.siguiente

			ultimo_nodo.siguiente = nuevo_nodo
		else:
			self.raiz = nuevo_nodo

	def imprimirLE(self):
		nodo_tmp = self.raiz
		while nodo_tmp != None:
			print(f" {nodo_tmp.dato} ", end="->")
			nodo_tmp = nodo_tmp.siguiente

		print(" Nulo")


	def buscarValor(self, datoBuscar):
		nodo_tmp = self.raiz
		while nodo_tmp != None:
			if nodo_tmp.dato == datoBuscar:
				print("Dato encontrado")
				break
			nodo_tmp = nodo_tmp.siguiente
		
		if nodo_tmp == None:		
			print("Dato no encontrado")

	def insertarAlInicio(self, nuevo_nodo):
		nuevo_nodo.siguiente = self.raiz
		self.raiz 			 = nuevo_nodo


	def borrarNodoPorPosicion(self,posicion):
		if self.raiz is None:
			print("Lista vacia")
			return

		indice = 0
		actual = self.raiz
		while actual.siguiente != None and indice < posicion:
			anterior 	= actual
			actual 		= actual.siguiente
			indice+=1

		if indice < posicion:
			print("Indice fuera rango")
		elif indice == 0:
			self.raiz = self.raiz.siguiente	
		else:
			anterior.siguiente = actual.siguiente
			actual = None

miListaEnlazada = ListaEnlazada()
n1 = nodo("a")
n2 = nodo("b")
n3 = nodo("c")
miListaEnlazada.insertarAlFinal(n1)
miListaEnlazada.insertarAlFinal(n2)
miListaEnlazada.insertarAlFinal(n3)
# miListaEnlazada.insertarAlInicio(nodo("cuarto"))
miListaEnlazada.imprimirLE()
miListaEnlazada.borrarNodoPorPosicion(5)
miListaEnlazada.imprimirLE()
miListaEnlazada.buscarValor("z")


#  TAMBIEN SE PUEDE BORRAR NODO POR EL VALOR 			SIMPLES, DOBLES, CIRCULARES
#  AGREGAR AL INICIO EN UNA 							SIMPLES, LISTA DOBLEMENTE ENLAZADA, CIRCULARES
#  ELIMINACION DE UN VALOR(POR POSICION) DE LA LISTA DOBLE ENLAZADA , CIRCULARES,SIMPLES