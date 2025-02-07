def isMonotonic(array):
    notDecrease, notIncrease = True, True
    for i in range(len(array) - 1):
        if array[i] < array[i + 1]:
            notDecrease = False
        elif array[i] > array[i + 1]:
            notIncrease = False
    return notIncrease or notDecrease


tests = [
    {
        "1": [-1, -5, -10, -1100, -1100, -1101, -1102, -9001],
        "expected": True
    },
    {
        "1": [1, 5, 10, 1100, 1101, 1102, 9001],
        "expected": True
    },
    {     
        "1": [1, 2, 0],
        "expected": False
    },
    {
        "1": [2, 2, 2, 1, 4, 5],
        "expected": False
    },
    {
        "1": [-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -8, -9, -10, -11],
        "expected": True
    }
]


for t in tests:
    res = isMonotonic(t["1"])
    if res != t["expected"]:
        print("result: ", res, ", expected: ", t["expected"])
    else:
        print("Ok")