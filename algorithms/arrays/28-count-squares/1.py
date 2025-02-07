# TC O(N^2)
# SC O(N)

def countSquares(points):
    squareNum = 0
    s = set()
    for p in points:
        s.add((p[0], p[1]))

    def buildRestSquarePoints(p1, p2):
        dX, dY = p2[0] - p1[0], p2[1] - p1[1]
        middleP = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
        p3 = (middleP[0] - dY / 2, middleP[1] + dX / 2)
        p4 = (middleP[0] + dY / 2, middleP[1] - dX / 2)
        return (p3, p4)        

    for i1 in range(len(points)):
        p1 = points[i1]
        for i2 in range(i1 + 1, len(points)):
            p2 = points[i2]
            p3, p4 = buildRestSquarePoints(p1, p2)
            if p3 in s and p4 in s:
                squareNum += 1
        s.remove((p1[0], p1[1]))
    return squareNum



tests = [
    {
        "points": [
            [1, 1],
            [3, -3],
            [0, 0],
            [0, 1],
            [-1, 3],
            [6, 2],
            [0, -2],
            [1, 0],
            [4, 0],
            [5, 1],
            [1, 5],
            [-2, 0]
        ],
        "expected": 3
    },
    {
        "points": [
            [21, 1],
            [3, 1],
            [1, 1],
            [21, 19],
            [0, 0],
            [0, 1],
            [2, 3],
            [22, 2],
            [3, 7],
            [1, 0],
            [12, -14],
            [-4, -2],
            [-22, 22],
            [27, -5],
            [-1, 3],
            [3, 5],
            [5, 1],
            [10, -19],
            [9, 1],
            [1, -1],
            [9, 7],
            [13, 12],
            [0, 7],
            [3, 19],
            [33, -2]
        ],
        "expected": 6
    },
    {
        "points": [
            [1, 1],
            [0, 0],
            [-4, 2],
            [-2, -1],
            [0, 1],
            [1, 0],
            [-1, 4]
        ],
        "expected": 2
    },
    {
        "points": [
            [1, 1],
            [0, 0],
            [0, 1],
            [1, 0]
        ],
        "expected": 1
    },
    {
        "points": [],
        "expected": 0
    }
]


for t in tests:
    res = countSquares(t["points"])
    if res != t["expected"]:
        print("result: ", res, ", expected: ", t["expected"])
    else:
        print("Ok")