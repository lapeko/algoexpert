def longestSubarrayWithSum(array, targetSum):
    sum, leftPtr, rightPtr = 0, 0, 0
    size = len(array)
    subArrayIndexes = []

    while rightPtr < size:
        sum += array[rightPtr]
        
        while sum > targetSum and leftPtr < rightPtr:
            sum -= array[leftPtr]
            leftPtr += 1

        if targetSum == sum:
            if len(subArrayIndexes) == 0 or subArrayIndexes[1] - subArrayIndexes[0] < rightPtr - leftPtr:
                subArrayIndexes = [leftPtr, rightPtr]
        
        rightPtr += 1
    return subArrayIndexes


tests = [
    {
        
        "1": [1, 2, 3, 4, 3, 3, 1, 2, 1],
        "2": 10,
        "expected": [4, 8]
    },
    {
        "1": [61, 54, 1, 499, 2212, 4059, 1, 2, 3, 1, 3],
        "2": 19,
        "expected": []
    },
    {
        "1": [1, 4, 10, 15, 31, 7, 1, 40, 0, 20, 1, 1, 1, 1, 2, 1],
        "2": 0,
        "expected": [8, 8]
    }
]


for t in tests:
    res = longestSubarrayWithSum(t["1"], t["2"])
    if res != t["expected"]:
        print("result: ", res, ", expected: ", t["expected"])
    else:
        print("Ok")