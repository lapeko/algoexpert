# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if not self.head:
            self.head = self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def setTail(self, node):
        # Write your code here.
        pass

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        pass

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        pass

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        pass

    def removeNodesWithValue(self, value):
        # Write your code here.
        pass

    def remove(self, node):
        # Write your code here.
        pass

    def containsNodeWithValue(self, value):
        # Write your code here.
        pass


def print_dll_forward(dll):
    head, values = dll.head, []
    while head:
        values.append(str(head.value))
        head = head.next
    print(" <-> ".join(values), " [from head]")

def print_dll_back(dll):
    tail, values = dll.tail, []
    while tail:
        values.append(str(tail.value))
        tail = tail.prev
    print(" <-> ".join(reversed(values)), " [from tail]")

def print_dll(dll):
    print_dll_forward(dll)
    print_dll_back(dll)

dll = DoublyLinkedList()
dll.setHead(Node(1))
print_dll(dll)
dll.setHead(Node(2))
dll.setHead(Node(3))
print_dll(dll)
