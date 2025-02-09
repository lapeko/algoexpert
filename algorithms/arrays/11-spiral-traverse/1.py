def spiralTraverse(array):
    res = []
    width, height = len(array[0]), len(array)
    x, y, step, size = -1, 0, 1, width * height

    while len(res) < size:
        for _ in range(width):
            x += step
            res.append(array[y][x])
        width -= 1
        height -= 1
        for _ in range(height):
            y += step
            res.append(array[y][x])
        step *= -1
        
    return res


tests = [
    {
        "array": [
            [1,  2,  3,  4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10, 9,  8,  7],
        ],
        "expected": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    },
]

for t in tests:
    res = spiralTraverse(t["array"])
    if res != t["expected"]:
        print("result: ", res, ", expected: ", t["expected"])
    else:
        print("Ok")