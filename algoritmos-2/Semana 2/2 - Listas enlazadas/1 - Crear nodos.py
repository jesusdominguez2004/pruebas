# Crear nodos
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


myNode = Node(10)
print(f"The data in the node is: {myNode.data}")
print(f"The next attribute in the node is: {myNode.next}")
