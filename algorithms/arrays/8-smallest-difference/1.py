def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    ptrOne = 0
    ptrTwo = 0
    minDif = [arrayOne[0], arrayTwo[0]]

    while ptrOne < len(arrayOne) and ptrTwo < len(arrayTwo):
        diff = absDiff(arrayOne[ptrOne], arrayTwo[ptrTwo])
        if diff < absDiff(minDif[0], minDif[1]):
            minDif = [arrayOne[ptrOne], arrayTwo[ptrTwo]]
        if ptrOne == len(arrayOne) - 1:
            ptrTwo += 1
            continue
        if ptrTwo == len(arrayTwo) - 1:
            ptrOne += 1
            continue
        diff1 = absDiff(arrayOne[ptrOne + 1], arrayTwo[ptrTwo])
        diff2 = absDiff(arrayOne[ptrOne], arrayTwo[ptrTwo + 1])
        if diff1 < diff2:
            ptrOne += 1
        else:
            ptrTwo += 1
    
    return minDif

def absDiff(a, b):
    return abs(a - b)

    




tests = [
    {
        "arrayOne": [-1, 5, 10, 20, 28, 3],
        "arrayTwo": [26, 134, 135, 15, 17],
        "expected": [28, 26],
    },
]


for t in tests:
    res = smallestDifference(t["arrayOne"], t["arrayTwo"])
    if res != t["expected"]:
        print("result: ", res, ", expected: ", t["expected"])
    else:
        print("Ok")