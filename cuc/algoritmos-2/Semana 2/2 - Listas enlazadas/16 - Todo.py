# Todo sobre listas enlazadas
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

    def insertAtBeginning(self, element):
        if self.Head is None:
            newNode = Node(element)
            self.Head = newNode
        else:
            newNode = Node(element)
            newNode.next = self.Head
            self.Head = newNode

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

    def deleteFromBeginning(self):
        if self.Head is None:
            print("The linked list empty. Cannot delete an element.")
            return
        else:
            node = self.Head
            self.Head = self.Head.next
            del node

    def deleteFromLast(self):
        if self.Head is None:
            print("The linked list empty. Cannot delete an element.")
            return
        else:
            current = self.Head
            previous = None
            while current.next is not None:
                previous = current
                current = current.next
            previous.next = None
            del current

    def deleteAtPosition(self, position):
        if self.Head is None:
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

    def countElements(self):
        count = 0
        current = self.Head
        while current is not None:
            count += 1
            current = current.next
        print("Number of elements in the linked list are:", count)

    def replaceElement(self, old_element, new_element):
        current = self.Head
        while current is not None:
            if current.data == old_element:
                current.data = new_element
                break
            current = current.next

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
            