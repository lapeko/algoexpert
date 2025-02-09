def longestPeak(array):
    start, peak, end, maxRange = 0, 0, 0, 0
    rising = True
    
    for i, curr in enumerate(array[:-1]):
        next = array[i + 1]
        if start < peak and peak < end:
            maxRange = max(maxRange, end - start + 1)
        if curr < next:
            peak = i + 1
            if not rising:
                rising = True
                start = i
        elif curr == next:
            start = i + 1
        else:
            end = i + 1
            rising = False

    if start < peak and peak < end:
        maxRange = max(maxRange, end - start + 1)

    return maxRange


tests = [
    {
        "array": [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3],
        "expected": 6,
    },
    {
        "array": [1, 2, 3, 3, 2, 1],
        "expected": 0,
    },
    {
        "array": [1, 3, 2],
        "expected": 3,
    },
]

for t in tests:
    res = longestPeak(t["array"])
    if res != t["expected"]:
        print("result: ", res, ", expected: ", t["expected"])
    else:
        print("Ok")