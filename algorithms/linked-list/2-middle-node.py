# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    fast = slow = linkedList
    while fast and fast.next:
        slow = slow.next
        fast = fast.next and fast.next.next
    return slow