# TC O(N2)
# SC O(N)

def minimumAreaRectangle(points):
    min, table = 0, {}
    for p in points:
        if p[0] not in table:
            table[p[0]] = set()
        table[p[0]].add(p[1])
    
    for k in list(table.keys()):
        if len(table[k]) < 2:
            del table[k]

    xS = list(table.keys())
    for idx1 in range(len(xS) - 1):
        x1 = xS[idx1]
        for idx2 in range(idx1 + 1, len(xS)):
            x2 = xS[idx2] 
            width = x2 - x1
            area = abs(width * getMinimalheight(table[x1], table[x2]))
            if area == 0:
                continue
            if min == 0:
                min = area
            if area < min:
                min = area    
    return min

def getMinimalheight(set1, set2):
    min = 0
    intersections = sorted(set1 & set2)
    
    if len(intersections) < 2:
        return min

    for i in range(1, len(intersections)):
        height = intersections[i - 1] - intersections[i]
        if height == 0:
            continue
        if min == 0:
            min = height
        if height < min:
            min = height
    return min



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