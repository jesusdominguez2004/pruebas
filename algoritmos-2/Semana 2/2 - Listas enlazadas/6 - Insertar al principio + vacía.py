# Insertar elemento al principio + vacía
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

    def insertAtBeginning(self, element):
        if self.Head is None:
            newNode = Node(element)
            self.Head = newNode
        else:
            newNode = Node(element)
            newNode.next = self.Head
            self.Head = newNode


myLinkedList = LinkedList()
myLinkedList.insertAtBeginning(10)
myLinkedList.insertAtBeginning(20)
myLinkedList.insertAtBeginning(30)
print("The elements in the linked list are: ")
myLinkedList.printList()
