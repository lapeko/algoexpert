def transposeMatrix(matrix):
    width, height = len(matrix[0]), len(matrix)
    res = [[0] * height for _ in range(width)]

    for i in range(height):
        for j in range(width):
            res[j][i] = matrix[i][j]

    return res


tests = [
    {
        "array": [
            [1, 4],
            [2, 5],
            [3, 6]
        ],
        "expected": [
            [1, 2, 3],
            [4, 5, 6]
        ]
    },
    {
        "array": [
            [1, 2],
        ],
        "expected": [
            [1],
            [2],
        ]
    }
]

for t in tests:
    res = transposeMatrix(t["array"])
    if res != t["expected"]:
        print(f"received: {res} expected: {t["expected"]}")
    else:
        print("OK")