def arrayOfProducts(array):
    res = [1]
    for n in array[:-1]:
        res.append(res[-1] * n)
    total = 1
    for i in reversed(range(0, len(array) - 1)):
        total *= array[i + 1]
        res[i] *= total
    return res

tests = [
    {
        "array": [5, 1, 4, 2],
        "expected": [8, 40, 10, 20],
    },
    {
        "array": [9, 3, 2, 1, 9, 5, 3, 2],
        "expected": [1620, 4860, 7290, 14580, 1620, 2916, 4860, 7290],
    },
    {
        "array": [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "expected": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    },
    {
        "array": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "expected": [362880, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    }
]

for t in tests:
    res = arrayOfProducts(t["array"])
    if res != t["expected"]:
        print("result: ", res, ", expected: ", t["expected"])
    else:
        print("Ok")