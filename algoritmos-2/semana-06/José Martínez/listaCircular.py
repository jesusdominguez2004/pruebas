class Nodo:
	def __init__(self, valor):  # metodo inicializador
		self.dato      = valor
		self.siguiente = None	#   none =  Null	

class ListaEnlazadaCircular:

	def __init__(self):
		self.raiz = None  # nodo principal


	def insertarAlFinal(self , nuevo_nodo):
		if self.raiz is not None:
			ultimo_nodo = self.raiz
			while ultimo_nodo.siguiente != self.raiz:
				ultimo_nodo = ultimo_nodo.siguiente

			ultimo_nodo.siguiente = nuevo_nodo
			nuevo_nodo.siguiente  = self.raiz
		else:
			self.raiz = nuevo_nodo
			self.raiz.siguiente = self.raiz

	def imprimirLE(self):
		if self.raiz is not None:
			nodo_tmp = self.raiz
			while True:
				print(f" {nodo_tmp.dato} ", end="->")
				nodo_tmp = nodo_tmp.siguiente
				if nodo_tmp == self.raiz:
					break

lc = ListaEnlazadaCircular()
N1 = Nodo("A")
N2 = Nodo("B")
N3 = Nodo("C")
lc.insertarAlFinal(N1)
lc.insertarAlFinal(N2)
lc.insertarAlFinal(N3)
lc.imprimirLE()
