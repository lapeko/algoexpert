# TC worst O(N) best O(log N)
# SC worst O(N) best O(log N)

import json

def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)

def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    if tree.value == target:
        return target
    if abs(tree.value - target) < abs(closest - target):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    return findClosestValueInBstHelper(tree.right, target, closest)

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def buildBST(treeData):
    nodes = {node["id"]: BST(node["value"]) for node in treeData["nodes"]}
    
    for node in treeData["nodes"]:
        if node["left"] is not None:
            nodes[node["id"]].left = nodes[node["left"]]
        if node["right"] is not None:
            nodes[node["id"]].right = nodes[node["right"]]
    
    return nodes[treeData["root"]]

jsonData = '''{
  "target": -70,
  "tree": {
    "nodes": [
      {"id": "100", "left": "5", "right": "502", "value": 100},
      {"id": "502", "left": "204", "right": "55000", "value": 502},
      {"id": "55000", "left": "1001", "right": null, "value": 55000},
      {"id": "1001", "left": null, "right": "4500", "value": 1001},
      {"id": "4500", "left": null, "right": null, "value": 4500},
      {"id": "204", "left": "203", "right": "205", "value": 204},
      {"id": "205", "left": null, "right": "207", "value": 205},
      {"id": "207", "left": "206", "right": "208", "value": 207},
      {"id": "208", "left": null, "right": null, "value": 208},
      {"id": "206", "left": null, "right": null, "value": 206},
      {"id": "203", "left": null, "right": null, "value": 203},
      {"id": "5", "left": "2", "right": "15", "value": 5},
      {"id": "15", "left": "5-2", "right": "22", "value": 15},
      {"id": "22", "left": null, "right": "57", "value": 22},
      {"id": "57", "left": null, "right": "60", "value": 57},
      {"id": "60", "left": null, "right": null, "value": 60},
      {"id": "5-2", "left": null, "right": null, "value": 5},
      {"id": "2", "left": "1", "right": "3", "value": 2},
      {"id": "3", "left": null, "right": null, "value": 3},
      {"id": "1", "left": "-51", "right": "1-2", "value": 1},
      {"id": "1-2", "left": null, "right": "1-3", "value": 1},
      {"id": "1-3", "left": null, "right": "1-4", "value": 1},
      {"id": "1-4", "left": null, "right": "1-5", "value": 1},
      {"id": "1-5", "left": null, "right": null, "value": 1},
      {"id": "-51", "left": "-403", "right": null, "value": -51},
      {"id": "-403", "left": null, "right": null, "value": -403}
    ],
    "root": "100"
  }
}'''
expectRes = -51
testData = json.loads(jsonData)



res = findClosestValueInBst(buildBST(testData["tree"]), testData["target"])
if res != expectRes:
    print("received:", res, "expected:", expectRes)
else:
    print("Ok")