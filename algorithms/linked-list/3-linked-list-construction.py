# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if not self.head:
            self.head = self.tail = node
        else:
            self.remove(node)
            self.head.prev = node
            node.next = self.head
            self.head = node

    def setTail(self, node):
        if not self.tail:
            self.head = self.tail = node
        else:
            self.remove(node)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def insertBefore(self, node, nodeToInsert):
        if not node.prev:
            self.setHead(nodeToInsert)
        else:
            self.remove(nodeToInsert)
            node.prev.next = nodeToInsert
            nodeToInsert.prev = node.prev
            nodeToInsert.next = node
            node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if not node.next:
            self.setTail(nodeToInsert)
        else:
            self.remove(nodeToInsert)
            node.next.prev = nodeToInsert
            nodeToInsert.next = node.next
            node.next = nodeToInsert
            nodeToInsert.prev = node

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            return self.setHead(nodeToInsert)
        node_at_position = self.head
        while position > 1:
            position -= 1
            node_at_position = node_at_position.next
        if nodeToInsert.next == node_at_position:
            return None # No changes should be done for case DoublyLinkedList[node1 <-> node2].insertAtPosition(2, node1)
        return self.insertBefore(node_at_position, nodeToInsert)

    def removeNodesWithValue(self, value):
        head = self.head
        while head:
            nxt = head.next
            if head.value == value:
                self.remove(head)
            head = nxt

    def remove(self, node):
        if self.head == node and self.tail == node:
            self.head = self.tail = None
        elif self.head == node:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail == node:
            self.tail = self.tail.prev
            self.tail.next = None
        elif node.next or node.prev:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.next = node.prev = None

    def containsNodeWithValue(self, value):
        head = self.head
        while head and head.value != value:
            head = head.next
        return head is not None



def list_dll(dll):
    head, values = dll.head, []
    while head:
        values.append(head.value)
        head = head.next
    return values

def list_dll_back(dll):
    tail, values = dll.tail, []
    while tail:
        values.append(tail.value)
        tail = tail.prev
    return values

def print_dll(dll):
    l1, l2 = list_dll(dll), list(reversed(list_dll_back(dll)))
    print(l1, "symmetric:", l1 == l2)

dll = DoublyLinkedList()

nodes = {str(i): Node(i) for i in range(1, 8)}

dll.setHead(nodes["1"])
dll.insertAfter(nodes["1"], nodes["2"])
dll.insertAfter(nodes["2"], nodes["3"])
dll.insertAfter(nodes["3"], nodes["4"])
dll.insertAfter(nodes["4"], nodes["5"])
dll.insertAfter(nodes["5"], nodes["6"])
dll.insertAfter(nodes["6"], nodes["7"])

print_dll(dll)  # [1, 2, 3, 4, 5, 6, 7]

dll.insertAtPosition(7, nodes["1"])
print_dll(dll)  # [2, 3, 4, 5, 6, 1, 7]

dll.insertAtPosition(1, nodes["1"])
print_dll(dll)  # [1, 2, 3, 4, 5, 6, 7]

dll.insertAtPosition(2, nodes["1"])
print_dll(dll)  # [1, 2, 3, 4, 5, 6, 7]

dll.insertAtPosition(3, nodes["1"])
print_dll(dll)  # [2, 1, 3, 4, 5, 6, 7]

dll.insertAtPosition(4, nodes["1"])
print_dll(dll)  # [2, 3, 1, 4, 5, 6, 7]

dll.insertAtPosition(5, nodes["1"])
print_dll(dll)  # [2, 3, 4, 1, 5, 6, 7]

dll.insertAtPosition(6, nodes["1"])
print_dll(dll)  # [2, 3, 4, 5, 1, 6, 7]
