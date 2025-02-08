def moveElementToEnd(array, toMove):
    leftPtr, rightPtr = 0, len(array) - 1
    while leftPtr < rightPtr:
        if array[leftPtr] != toMove:
            leftPtr += 1
        elif array[rightPtr] == toMove:
            rightPtr -= 1
        else:
            array[leftPtr], array[rightPtr] = array[rightPtr], array[leftPtr]
    return array
        


tests = [
    {
        "1": [2, 1, 2, 2, 2, 3, 4, 2],
        "2": 2,
        "expected": [4, 1, 3, 2, 2, 2, 2, 2]
    },
    {
        "1": [],
        "2": 3,
        "expected": []
    },
    {     
        "1": [1, 2, 3, 4, 5],
        "2": 3,
        "expected": [1, 2, 5, 4, 3]
    },
    {
        "1": [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 5, 5, 5, 5, 5, 5],
        "2": 5,
        "expected": [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 5, 5, 5, 5, 5, 5]
    }
]


for t in tests:
    res = moveElementToEnd(t["1"], t["2"])
    if res != t["expected"]:
        print("result: ", res, ", expected: ", t["expected"])
    else:
        print("Ok")