# Reemplazar todos los valores en lista enlazada
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

    def replaceElements(self, old_element, new_element):
        current = self.Head
        while current is not None:
            if current.data == old_element:
                current.data = new_element
            current = current.next

myLinkedList = LinkedList()
myLinkedList.insertAtPosition(20, 1)
myLinkedList.insertAtPosition(20, 2)
myLinkedList.insertAtPosition(30, 3)
myLinkedList.insertAtPosition(40, 2)
print("The elements in the linked list are: ")
myLinkedList.printList()
myLinkedList.replaceElements(30, 100)
print("The elements in the linked list are: ")
myLinkedList.printList()
myLinkedList.replaceElement(20, 150)
print("The elements in the linked list are: ")
myLinkedList.printList()
