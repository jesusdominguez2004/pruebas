# Eliminar en posición dada
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
        print("")

    def insertAtPosition(self, element, position):
        counter = 1
        current = self.Head
        while counter < position - 1 and current is not None:
            counter += 1
            current = current.next
        if position == 1:
            newNode = Node(element)
            newNode.next = current
            self.Head = newNode
        else:
            newNode = Node(element)
            newNode.next = current.next
            current.next = newNode

    def deleteAtPosition(self, position):
        if self.Head == None:
            print("The linked list empty. Cannot delete an element.")
            return
        else:
            current = self.Head
            previous = None
            count = 1
            while current.next is not None and count < position:
                previous = current
                current = current.next
                count += 1
            if current == self.Head:
                self.Head = current.next
                del current
            else:
                previous.next = current.next
                del current


myLinkedList = LinkedList()
myLinkedList.insertAtPosition(10, 1)
myLinkedList.insertAtPosition(20, 2)
myLinkedList.insertAtPosition(30, 3)
myLinkedList.insertAtPosition(40, 2)
print("The elements in the linked list are: ")
myLinkedList.printList()
myLinkedList.deleteAtPosition(1)
print("The elements in the linked list are: ")
myLinkedList.printList()
myLinkedList.deleteAtPosition(2)
print("The elements in the linked list are: ")
myLinkedList.printList()
