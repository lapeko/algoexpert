# TC O(log N) best. O(N) worst
# SC O(log N) best. O(N) worst (because of recursion)
# TODO implement SC(1)

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        branch = self.right
        if value < self.value:
            branch = self.left
        if branch is not None:
            return branch.insert(value)
        if value < self.value:
            self.left = BST(value)
        else:
            self.right = BST(value)
        return self

    def contains(self, value):
        if self.value == value:
            return True
        branch = self.right
        if value < self.value:
            branch = self.left
        if branch is None:
            return False
        return branch.contains(value)

    def remove(self, value):
        if value == self.value:
            self._deleteNotEmpty()
        elif value < self.value:
            if self.left is not None:
                if self.left.value == value and self.left.left is None and self.left.right is None:
                    self.left = None
                else:
                    self.left.remove(value)
        else:
            if self.right is not None:
                if self.right.value == value and self.right.left is None and self.right.right is None:
                    self.right = None
                else:
                    self.right.remove(value)
        return self

    def _cutClosest(self):
        if self.left.left is not None:
            return self.left._cutClosest()
        value = self.left.value
        self.left = self.left.right
        return value

    def _deleteNotEmpty(self):
        left = self.left
        right = self.right
        if left == right:
            self = None
        elif right == None:
            self.value = left.value
            self.left = left.left
            self.right = left.right
        elif left == None:
            self.value = right.value
            self.right = right.right
            self.left = right.left
        elif right.left is None:
            self.value = right.value
            self.right = right.right
        else:
            self.value = self.right._cutClosest()
        return self


test = {
  "classMethodsToCall": [
    {"arguments": [5], "method": "insert"},
    {"arguments": [15], "method": "insert"},
    {"arguments": [3], "method": "insert"},
    {"arguments": [7], "method": "insert"},
    {"arguments": [12], "method": "insert"},
    {"arguments": [18], "method": "insert"},
    {"arguments": [11], "method": "insert"},
    {"arguments": [13], "method": "insert"},
    {"arguments": [14], "method": "insert"},
    {"arguments": [10], "method": "remove"}
  ],
  "rootValue": 10
}

bst = BST(test["rootValue"])
for callData in test["classMethodsToCall"]:
    method = getattr(bst, callData["method"])
    method(callData["arguments"][0])

print("Root:", bst.value)  # 11
print("Root Left:", bst.left.value)  # 5
print("Root Right:", bst.right.value)  # 15
print("Right Left:", bst.right.left.value)  # 12
print("Right Left Left:", bst.right.left.left)  # None
print("Right Left Right:", bst.right.left.right.value)  # 13
print("Right Left Right Right:", bst.right.left.right.right.value)  # 14

