# TC O(N2)
# SC O(N)

def minimumAreaRectangle(points):
    minArea = 0
    pointsMap = {}

    for p in points:
        if p[0] not in pointsMap:
            pointsMap[p[0]] = set()
        pointsMap[p[0]].add(p[1])

    for idx1 in range(len(points) - 1):
        for idx2 in range(idx1 + 1, len(points)):
            p1, p2 = points[idx1], points[idx2]
            if p1[0] == p2[0] or p1[1] == p2[1]:
                continue
            if p1[1] not in pointsMap[p2[0]] or p2[1] not in pointsMap[p1[0]]:
                continue
            area = abs((p2[0] - p1[0]) * (p2[1] - p1[1]))
            if minArea == 0 or area < minArea:
                minArea = area
    return minArea



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