# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def zipLinkedList(linkedList):
    if not linkedList.next:
        return linkedList

    prev_slow = slow = fast = linkedList

    while fast and fast.next:
        prev_slow = slow
        slow = slow.next
        fast = fast.next.next
    prev_slow.next = None

    left, right = linkedList, reverse_linked_list(slow)
    while left and right:
        next_left, next_right = left.next, right.next
        left.next = right
        if next_left:
            right.next = next_left
        left, right = next_left, next_right
    return linkedList

def reverse_linked_list(head):
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev

def run_tests():
    tests = [{
        "payload": [1, 2, 3, 4, 5],
        "expected": [1, 5, 2, 4, 3]
    }, {
        "payload": [1, 2, 3, 4, 5, 6],
        "expected": [1, 6, 2, 5, 3, 4]
    }, {
        "payload": [1],
        "expected": [1]
    }, {
        "payload": [1, -6, 8, 5, 10, -1, 0, 2, 11, -100, 99, 50],
        "expected": [1, 50, -6, 99, 8, -100, 5, 11, 10, 2, -1, 0]
    }]
    for t in tests:
        ll = build_linked_list_from_list(t["payload"])
        res = linked_list_to_list(zipLinkedList(ll))
        if res == t["expected"]:
            print("OK")
        else:
            print(f"res: {res}. expected: {t["expected"]}")

def iterable_linked_list(linked_list):
    while linked_list:
        yield linked_list.value
        linked_list = linked_list.next

def linked_list_to_list(linked_list):
    return [n for n in iterable_linked_list(linked_list)]

def build_linked_list_from_list(nums):
    ll = LinkedList(nums[0])
    current = ll
    for n in nums[1:]:
        current.next = LinkedList(n)
        current = current.next
    return ll

run_tests()