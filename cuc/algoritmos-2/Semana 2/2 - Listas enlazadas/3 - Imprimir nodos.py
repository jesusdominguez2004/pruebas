# Imprimir nodos
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.Head = None

    def printList(self):
        current = self.Head
        while current is not None:
            print(current.data, end=" ")
            current = current.next


myLinkedList = LinkedList()
myNode1 = Node(10)
myNode2 = Node(20)
myNode3 = Node(30)
myNode4 = Node(40)
myLinkedList.Head = myNode1
myNode1.next = myNode2
myNode2.next = myNode3
myNode3.next = myNode4

print("The elements in the linked list are: ")
myLinkedList.printList()
