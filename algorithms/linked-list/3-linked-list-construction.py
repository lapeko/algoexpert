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
        # Write your code here.
        pass

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



def print_list(dll, label=""):
    current = dll.head
    out = []
    while current:
        out.append(current.value)
        current = current.next
    print(f"{label} -> {'->'.join(map(str, out)) if out else 'EMPTY'}")


dll = DoublyLinkedList()

print("\n=== REMOVE HEAD ===")
n1 = Node(1)
dll.setHead(n1)
dll.removeNodesWithValue(1)
print_list(dll, "Expected: EMPTY")

dll = DoublyLinkedList()
print("\n=== REMOVE TAIL ===")
n1 = Node(1)
n2 = Node(2)
dll.setHead(n1)
dll.setTail(n2)
dll.removeNodesWithValue(2)
print_list(dll, "Expected: 1")

dll = DoublyLinkedList()
print("\n=== REMOVE ONLY NODE ===")
n1 = Node(1)
dll.setHead(n1)
dll.removeNodesWithValue(1)
print_list(dll, "Expected: EMPTY")

dll = DoublyLinkedList()
print("\n=== REMOVE CONSECUTIVE VALUES ===")
n1 = Node(1)
n2 = Node(2)
n3 = Node(2)
n4 = Node(2)
n5 = Node(3)
dll.setHead(n1)
dll.setTail(n5)
dll.insertAfter(n1, n2)
dll.insertAfter(n2, n3)
dll.insertAfter(n3, n4)
print_list(dll, "Before remove")
dll.removeNodesWithValue(2)
print_list(dll, "Expected: 1->3")

dll = DoublyLinkedList()
print("\n=== REMOVE HEAD+TAIL ===")
n1 = Node(5)
n2 = Node(2)
n3 = Node(3)
n4 = Node(5)
dll.setHead(n1)
dll.setTail(n4)
dll.insertAfter(n1, n2)
dll.insertAfter(n2, n3)
print_list(dll, "Before remove")
dll.removeNodesWithValue(5)
print_list(dll, "Expected: 2->3")

dll = DoublyLinkedList()
print("\n=== REMOVE MULTIPLE MIDDLE ===")
n1 = Node(0)
n2 = Node(2)
n3 = Node(2)
n4 = Node(2)
n5 = Node(9)
dll.setHead(n1)
dll.setTail(n5)
dll.insertAfter(n1, n2)
dll.insertAfter(n2, n3)
dll.insertAfter(n3, n4)
print_list(dll, "Before remove")
dll.removeNodesWithValue(2)
print_list(dll, "Expected: 0->9")
