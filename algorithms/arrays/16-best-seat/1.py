# TC O(N)
# SC O(N)

def firstDuplicateValue(array):
    seatSet = set()
    for seat in array:
        if seat in seatSet:
            return seat
        seatSet.add(seat)
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