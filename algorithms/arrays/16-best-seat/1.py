def bestSeat(seats):
    freeSeatsInARow, bestSpaceAmount, bestSpaceStartIdx = 0, 0, -1
    for idx, num in enumerate(seats):
        if num == 1:
            freeSeatsInARow = 0
        else:
            freeSeatsInARow += 1
            if bestSpaceAmount < freeSeatsInARow:
                bestSpaceAmount = freeSeatsInARow
                bestSpaceStartIdx = idx
    return bestSpaceStartIdx - bestSpaceAmount // 2

tests = [
    {
        "array":  [1, 0, 1, 0, 0, 0, 1],
        "expected": 4,
    },
    {
        "array": [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        "expected": 6
    },
    {
        "array": [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
        "expected": 3
    }
]

for t in tests:
    res = bestSeat(t["array"])
    if res != t["expected"]:
        print("result: ", res, ", expected: ", t["expected"])
    else:
        print("Ok")