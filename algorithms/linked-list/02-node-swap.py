# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def nodeSwap(head):
    left = head
    while left and left.next:
        right = left.next
        left.value, right.value = right.value, left.value
        left = right.next
    return head

nodes = [0,1,2,3,4,5]
expected = [1, 0, 3, 2, 5, 4]
result = []

ll = LinkedList(nodes[0])
node = ll
for n in nodes[1:]:
    node.next = LinkedList(n)
    node = node.next

ll = nodeSwap(ll)

current = ll
while current:
    result.append(current.value)
    current = current.next

print(result == expected)