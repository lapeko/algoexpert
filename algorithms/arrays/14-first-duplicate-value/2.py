# TC O(N)
# SC O(1)

def firstDuplicateValue(array):
    for seat in array:
        absSeat = abs(seat)
        if array[absSeat - 1] < 0:
            return absSeat
        array[absSeat - 1] *= -1
    return -1

tests = [
    {
        "array": [2, 1, 5, 2, 3, 3, 4],
        "expected": 2,
    },
]

for t in tests:
    res = firstDuplicateValue(t["array"])
    if res != t["expected"]:
        print("result: ", res, ", expected: ", t["expected"])
    else:
        print("Ok")