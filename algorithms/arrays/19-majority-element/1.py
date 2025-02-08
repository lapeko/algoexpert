def majorityElement(array):
    for i, num in enumerate(array):
        numAppereances = 1
        for j in range(i + 1, len(array)):
            if num == array[j]:
                numAppereances += 1
        if numAppereances > len(array) / 2:
            return num
    return -1


tests = [
    {
        "input": [],
        "expected": -1
    },
    {
        "input": [1],
        "expected": 1
    },
    {
        "input": [0, 1],
        "expected": -1
    },
    {
        "input": [1, 0, 5, 3, 3, 3, 3, 3, 1],
        "expected": 3
    },
    {
        "input": [1, 1, 2, 2, 3],
        "expected": -1
    },
]

for t in tests:
    res = majorityElement(t["input"])
    if res != t["expected"]:
        print(f"expected: {t["expected"]}, received: {res}")
    else:
        print("OK")