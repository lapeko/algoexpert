# TC O(N2)
# SC O(N)

def minimumAreaRectangle(points):
    minArea, table = 0, {}
    for p in points:
        if p[0] not in table:
            table[p[0]] = set()
        table[p[0]].add(p[1])
    
    for k in list(table.keys()):
        if len(table[k]) < 2:
            del table[k]

    xS = sorted(list(table.keys()))
    for idx in range(len(xS) - 1):
        x1 = xS[idx]
        x2 = xS[idx + 1]
        width = x2 - x1
        area = abs(width * getMinimalHeight(table[x1], table[x2]))
        if area == 0:
            continue
        if minArea == 0:
            minArea = area
        if area < minArea:
            minArea = area        
    return minArea

def getMinimalHeight(set1, set2):
    minHeight = 0
    intersections = sorted(set1 & set2)
    
    if len(intersections) < 2:
        return minHeight

    for i in range(1, len(intersections)):
        height = intersections[i - 1] - intersections[i]
        if height == 0:
            continue
        if minHeight == 0:
            minHeight = height
        if height < minHeight:
            minHeight = height
    return minHeight



tests = [
    {
        "array": [
            [1, 5],
            [5, 1],
            [4, 2],
            [2, 4],
            [2, 2],
            [1, 2],
            [4, 5],
            [2, 5],
            [-1, -2]
        ],
        "expected": 3
    },
    {
        "array": [
             [0, 0],
            [1, 1],
            [2, 2],
            [-1, -1],
            [-2, -2],
            [-1, 1],
            [-2, 2],
            [1, -1],
            [2, -2]
        ],
        "expected": 4
    }
]


for t in tests:
    res = minimumAreaRectangle(t["array"])
    if res != t["expected"]:
        print("result: ", res, ", expected: ", t["expected"])
    else:
        print("Ok")