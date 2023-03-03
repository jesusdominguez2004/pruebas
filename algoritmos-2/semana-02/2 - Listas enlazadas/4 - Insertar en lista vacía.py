# Insertar elemento en lista enlazada vacía
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

    def insertIntoEmptyList(self, element):
        newNode = Node(element)
        self.Head = newNode


myLinkedList = LinkedList()
myLinkedList.insertIntoEmptyList(10)

print("The elements in the linked list are: ")
myLinkedList.printList()
