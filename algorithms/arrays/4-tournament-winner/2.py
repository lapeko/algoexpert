def sortedSquaredArray(array):
    left, right = 0, len(array) - 1
    size = len(array)
    res = [0] * size

    for idx in range(size):
        lSqr = array[left] ** 2
        rSqr = array[right] ** 2
        if lSqr > rSqr:
            res[size - idx - 1] = lSqr
            left += 1
        else:
            res[size - idx - 1] = rSqr
            right -= 1

    return res

tests = [
    {
        "array": [-7, -3, 1, 9, 22, 30],
        "expected": [1, 9, 49, 81, 484, 900]
    },
    {
        "array": [1, 2, 3, 5, 6, 8, 9],
        "expected": [1, 4, 9, 25, 36, 64, 81]
    },
]

for t in tests:
    res = sortedSquaredArray(t["array"])
    if res != t["expected"]:
        print("result: ", res, ", expected: ", t["expected"])
    else:
        print("Ok")