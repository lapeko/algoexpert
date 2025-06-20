class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SingleLinkedList:
    def __init__(self, init_list = ()):
        self._length = 0
        if init_list:
            self.head = ListNode(init_list[0])
            last = self.head
            for val in init_list[1:]:
                last.next = ListNode(val)
                last = last.next
            self._length = len(init_list)
        else:
            self.head = None

    def __str__(self):
        current = self.head
        values = []
        while current:
            values.append(current.value)
            current = current.next
        return " -> ".join(map(str, values))

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next
            
    def __len__(self):
        return self._length

    def _get_node(self, index = -1):
        current = self.head
        idx = 0
        while current.next and not idx == index:
            idx += 1
            current = current.next
        return current


    def append(self, val):
        if len(self) == 0:
            self.head = ListNode(val)
            self._length += 1
            return
        last = self._get_node()
        last.next = ListNode(val)
        self._length += 1

    def prepend(self, val):
        new_header = ListNode(val)
        new_header.next = self.head
        self.head = new_header
        self._length += 1

    def insert(self, index, val):
        if index > len(self):
            raise ValueError(f"Provided index {index} is higher then the linked list size {len(self)}")
        if index == 0:
            tail = self.head
            self.head = ListNode(val)
            self.head.next = tail
        else:
            node = self._get_node(index - 1)
            tail = node.next
            node.next = ListNode(val)
            node.next.next = tail
        self._length += 1

    def delete(self, val):
        if not self.head:
            return False
        if self.head.value == val:
            self._length -= 1
            self.head = self.head.next
            return True
        current = self.head
        while current.next:
            if current.next.value == val:
                current.next = current.next.next
                self._length -= 1
                return True
            current = current.next
        return False

    def find(self, val):
        current = self.head
        while current:
            if current.value == val:
                return True
            current = current.next
        return False

    def to_list(self):
        current = self.head
        result = []
        while current:
            result.append(current.value)
            current = current.next
        return result

    def reverse(self):
        values = self.to_list()
        values.reverse()
        current = self.head
        for v in values:
            current.value = v
            current = current.next

    def pop(self):
        if len(self) == 0:
            raise Exception("SingleLinkedList is empty")
        if len(self) == 1:
            val = self.head.value
            self.head = None
            self._length -= 1
            return val
        node = self._get_node(len(self) - 2)
        val = node.next.value
        node.next = None
        self._length -= 1
        return val


sll = SingleLinkedList([1, 3, 5])
print(sll)                     # 1 -> 3 -> 5
print(len(sll))                # 3

sll.append(7)
print(sll)                     # 1 -> 3 -> 5 -> 7
print(len(sll))                # 4

sll.prepend(0)
print(sll)                     # 0 -> 1 -> 3 -> 5 -> 7
print(len(sll))                # 5

sll.insert(2, 2)
print(sll)                     # 0 -> 1 -> 2 -> 3 -> 5 -> 7
print(len(sll))                # 6

print(sll.find(3))             # True
print(sll.find(42))            # False

print(sll.delete(3))           # True
print(sll)                     # 0 -> 1 -> 2 -> 5 -> 7
print(sll.delete(999))         # False
print(len(sll))                # 5

print(sll.to_list())           # [0, 1, 2, 5, 7]

sll.reverse()
print(sll)                     # 7 -> 5 -> 2 -> 1 -> 0

print(sll.pop())               # 0
print(sll.pop())               # 1
print(sll)                     # 7 -> 5 -> 2
print(len(sll))                # 3

empty = SingleLinkedList()
print(empty)                   # (empty)

try:
    empty.pop()
except Exception as e:
    print(e)                   # SingleLinkedList is empty

try:
    sll.insert(999, 42)
except ValueError as e:
    print(e)                   # Provided index 999 is higher than...
