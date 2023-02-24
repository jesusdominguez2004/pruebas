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

    def insertAtEnd(self, element):
        if self.Head is None:
            newNode = Node(element)
            self.Head = newNode
        else:
            current = self.Head
            while current.next is not None:
                current = current.next
            newNode = Node(element)
            current.next = newNode


myLinkedList = LinkedList()
myLinkedList.insertAtEnd(10)
myLinkedList.insertAtEnd(20)
myLinkedList.insertAtEnd(30)
print("The elements in the linked list are: ")
myLinkedList.printList()
