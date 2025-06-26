# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Two pass solution. O(N) time, O(1) Space
# def removeKthNodeFromEnd(head, k):
#     current, size = head, 0
#     while current:
#         size += 1
#         current = current.next
#     current, position = head, size - k
#     if position == 0:
#         head.value = head.next.value
#         head.next = head.next.next
#     else:
#         for _ in range(position - 1):
#             current = current.next
#         current.next = current.next.next

# One pass solution. O(N) time, O(1) Space
def removeKthNodeFromEnd(head, k):
    slow_prev, slow, fast = None, head, head
    for _ in range(k):
        fast = fast.next
    while fast:
        slow_prev = slow
        slow = slow.next
        fast = fast.next
    if slow_prev is None:
        slow.value = slow.next.value
        slow.next = slow.next.next
    else:
        slow_prev.next = slow.next


def run_tests():
    def ll_to_list(ll):
        c = ll
        values = []
        while c:
            values.append(c.value)
            c = c.next
        return values

    head = LinkedList(0)
    current = head
    for n in range(1, 10):
        current.next = LinkedList(n)
        current = current.next

    print(ll_to_list(head))
    removeKthNodeFromEnd(head, 10)
    print(ll_to_list(head))


run_tests()
