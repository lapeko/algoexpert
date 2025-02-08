def largestRange(array):
    result = [array[0], array[0]]
    setOfAll = set(array)
    
    for num in array:
        if num in setOfAll:
            currentMin = currentMax = num
            setOfAll.remove(num)
            checkNum = num - 1
            while checkNum in setOfAll:
                currentMin = checkNum
                setOfAll.remove(checkNum)
                checkNum -= 1
            checkNum = num + 1
            while checkNum in setOfAll:
                currentMax = checkNum
                setOfAll.remove(checkNum)
                checkNum += 1
        if currentMax - currentMin > result[1] - result[0]:
            result = [currentMin, currentMax]
    return result
            

        




tests = [
    {
        "1": [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6],
        "expected": [0, 7]
    },
    {
        "1": [1],
        "expected": [1, 1]
    },
    {     
        "1": [-7, -7, -7, -7, 8, -8, 0, 9, 19, -1, -3, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, -6, 8, 7, 6, 15, 12, 12, -5, 2, 1, 6, 13, 14, -4, -2],
        "expected": [-8, 19]
    },
    {
        "1": [10, 0, 1],
        "expected": [0, 1]
    }
]


for t in tests:
    res = largestRange(t["1"])
    if res != t["expected"]:
        print("result: ", res, ", expected: ", t["expected"])
    else:
        print("Ok")