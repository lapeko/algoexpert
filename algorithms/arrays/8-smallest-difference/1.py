# TC O(N log N + M log M)
# SC O(1)

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    ptrOne, ptrTwo = 0, 0
    minDif = abs(arrayOne[0] - arrayTwo[0])
    minDifArr = [arrayOne[0], arrayTwo[0]]
    while ptrOne < len(arrayOne) and ptrTwo < len(arrayTwo):
        one, two = arrayOne[ptrOne], arrayTwo[ptrTwo]
        diff = abs(one - two)
        if one < two:
            ptrOne += 1
        else:
            ptrTwo += 1
        if diff < minDif:
            minDifArr = [one, two]
            minDif = diff
    return minDifArr


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