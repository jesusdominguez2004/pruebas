class Vertice:
	def __init__(self, valor):
		self.valor = valor
		
class Grafo:

	def __init__(self, dirigido = False):
		self.grafo 		= {}
		self.dirigido   = dirigido

	def agregar(self, vrt):
		self.grafo.update({vrt.valor: [] })

	def agregar_arista(self, vrt1 , vrt2, peso = 1):
		self.relacionar_arista(vrt1, vrt2, peso)

	def relacionar_arista(self, origen , destino, peso):
		self.grafo[origen.valor].append([destino.valor, peso])
		if self.dirigido == False:
			self.grafo[destino.valor].append([destino.valor, peso])


A = Vertice("A")
B = Vertice("B")
Z = Vertice("Z")
GR = Grafo(True);
print(GR.grafo)
GR.agregar(A)
GR.agregar(B)
GR.agregar(Z)
print(GR.grafo)

GR.agregar_arista(A, B)
GR.agregar_arista(A, Z)
print(GR.grafo)