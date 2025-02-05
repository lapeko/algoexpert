def sortedSquaredArray(array):
    return sorted([x ** 2 for x in array])

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
        print(res, "!=", t["expected"])
    else:
        print("Ok")