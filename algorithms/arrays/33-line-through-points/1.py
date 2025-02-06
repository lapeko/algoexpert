# TC O(N^2)
# SC O(N)

def lineThroughPoints(points):
    maxNumOfPoints = 1
    for idx1 in range(len(points) - 1):
        anglePointsNum = {}
        p1 = points[idx1]
        for idx2 in range(idx1 + 1, len(points)):
            p2 = points[idx2]
            dY = p1[1] - p2[1]
            if dY == 0:
                angle = float("inf")
            else:
                angle = (p1[0] - p2[0]) / dY
            if angle not in anglePointsNum:
                anglePointsNum[angle] = 1
            anglePointsNum[angle] += 1
            if anglePointsNum[angle] > maxNumOfPoints:
                maxNumOfPoints = anglePointsNum[angle]
    return maxNumOfPoints


tests = [
    {
        "array": [
            [1, 1],
            [2, 2],
            [3, 3],
            [0, 4],
            [-2, 6],
            [4, 0],
            [2, 1]
        ],
        "expected": 4
    },
    {
        "array": [
            [1, 1],
        ],
        "expected": 1
    },
    {
        "array": [
            [-1, -1],
            [-3, -1],
            [-4, -1],
            [1, 1],
            [4, 1]
        ],
        "expected": 3
    },
]



for t in tests:
    res = lineThroughPoints(t["array"])
    if res != t["expected"]:
        print("result: ", res, ", expected: ", t["expected"])
    else:
        print("Ok")
