# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    currentNode = None
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    currentNode = None
                else:
                    currentNode = currentNode.right
        return self

    def contains(self, value):
        while self is not None:
            if value < self.value:
                self = self.left
            elif value > self.value:
                self = self.right
            else:
                return True
        return False

    def remove(self, value):
        if self.value == value:
            res = handleTreeDeletion(self)
            if res is not None:
                self.value, self.left, self.right = res.value, res.left, res.right
            return self
        current, prev = self, self
        while current is not None:
            prev = current
            if value < current.value:
                current = current.left
                if current is None:
                    return self
                if current.value == value:
                    prev.left = handleTreeDeletion(current)
            else:
                current = current.right
                if current is None:
                    return self
                if current.value == value:
                    prev.right = handleTreeDeletion(current)

def handleTreeDeletion(tree):
    prev = rightTop = tree.right
    leftTop = tree.left
    if rightTop is None and leftTop is None:
        return None
    if rightTop is None:
        return leftTop
    bottomLeft = rightTop.left
    if bottomLeft is None:
        rightTop.left = tree.left
        return rightTop
    while bottomLeft is not None:
        rightTop = prev
        prev = bottomLeft
        bottomLeft = bottomLeft.left
    tree.value = prev.value
    rightTop.left = prev.right
    return tree
            
        



test = {
  "classMethodsToCall": [
    {"arguments": [5], "method": "insert"},
    {"arguments": [15], "method": "insert"},
    # {"arguments": [3], "method": "insert"},
    # {"arguments": [7], "method": "insert"},
    # {"arguments": [12], "method": "insert"},
    # {"arguments": [18], "method": "insert"},
    # {"arguments": [11], "method": "insert"},
    # {"arguments": [13], "method": "insert"},
    # {"arguments": [14], "method": "insert"},
    {"arguments": [10], "method": "remove"},
    # {"arguments": [5], "method": "remove"},
    # {"arguments": [15], "method": "remove"},
  ],
  "rootValue": 10
}

bst = BST(test["rootValue"])
for callData in test["classMethodsToCall"]:
    method = getattr(bst, callData["method"])
    method(callData["arguments"][0])

# print("Root:", bst.value)  # 11
# print("Root Left:", bst.left.value)  # 5
# print("Root Right:", bst.right.value)  # 15
# print("Right Left:", bst.right.left.value)  # 12
# print("Right Left Left:", bst.right.left.left)  # None
# print("Right Left Right:", bst.right.left.right.value)  # 13
# print("Right Left Right Right:", bst.right.left.right.right.value)  # 14
print(bst.contains(10))