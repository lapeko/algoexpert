def longestSubarrayWithSum(array, targetSum):
    leftPtr, rightPtr = 0, 0
    
    size = len(array)
    sum = array[0]
    subArrayIndexes = []

    while rightPtr < size:
        if sum < targetSum:
            rightPtr += 1
            if rightPtr < size:
                sum += array[rightPtr]
            continue
        
        if sum > targetSum:
            if leftPtr == rightPtr:
                leftPtr += 1
                rightPtr += 1
                if rightPtr < size:
                    sum = array[leftPtr]
            else:
                sum -= array[leftPtr]
                leftPtr += 1
            continue

        keptIdxDiff = -1 if len(subArrayIndexes) < 2 else subArrayIndexes[1] - subArrayIndexes[0]
        if keptIdxDiff < rightPtr - leftPtr:
            subArrayIndexes = [leftPtr, rightPtr]

        rightPtr += 1
        if rightPtr < size:
            sum += array[rightPtr]

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