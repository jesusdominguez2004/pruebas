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

    def updateAtPosition(self, new_element, position):
        if self.Head is None and position != 1:
            print("No element to update in the linked list.")
            return
        elif self.Head is None and position == 1:
            newNode = Node(new_element)
            self.Head = newNode
            return
        count = 1
        current = self.Head
        while current.next is not None and count < position:
            count += 1
            current = current.next
        if count == position:
            current.data = new_element
        elif current.next is None:
            print("Not enough elements in the linked list.")

myLinkedList = LinkedList()
myLinkedList.insertAtPosition(20, 1)
myLinkedList.insertAtPosition(20, 2)
myLinkedList.insertAtPosition(30, 3)
myLinkedList.insertAtPosition(40, 2)
print("The elements in the linked list are:")
myLinkedList.printList()
myLinkedList.updateAtPosition(100, 3)
print("The elements in the linked list are:")
myLinkedList.printList()
myLinkedList.updateAtPosition(150, 12)
print("The elements in the linked list are:")
myLinkedList.printList()
