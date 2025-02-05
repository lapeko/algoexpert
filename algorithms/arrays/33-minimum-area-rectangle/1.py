# TC O(N4)
# SC O(1)

def minimumAreaRectangle(points):
    min = 0
    found = False

    for idx1 in range(len(points) - 3):
        for idx2 in range(idx1 + 1, len(points) - 2):
            for idx3 in range(idx2 + 1, len(points) - 1):
                for idx4 in range(idx3 + 1, len(points)):
                    p1, p2, p3, p4 = points[idx1], points[idx2], points[idx3], points[idx4]
                    setX = set([p1[0], p2[0], p3[0], p4[0]])
                    if len(setX) != 2:
                        continue
                    setY = set([p1[1], p2[1], p3[1], p4[1]])
                    if len(setY) != 2:
                        continue
                    x1, x2 = setX
                    y1, y2 = setY
                    sq = abs((x1 - x2) * (y1 - y2))
                    if sq == 0:
                        continue
                    if not found:
                        min = sq
                        found = True
                    if sq < min:
                        min = sq
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
    }
]


for t in tests:
    res = minimumAreaRectangle(t["array"])
    if res != t["expected"]:
        print("result: ", res, ", expected: ", t["expected"])
    else:
        print("Ok")