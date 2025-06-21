# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    current = linkedList
    while current.next:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next
    return linkedList

nodes = [1, 1, 1, 3, 4, 4, 4, 5, 6, 6]

ll = LinkedList(nodes[0])
last = ll
for n in nodes[1:]:
    last.next = LinkedList(n)
    last = last.next

ll = removeDuplicatesFromLinkedList(ll)

node = ll
while node:
    print(node.value)
    node = node.next
