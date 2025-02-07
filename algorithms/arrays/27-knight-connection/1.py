def knightConnection(knightA, knightB):
    moves = 0
    s1, s2 = set(), set()
    s1.add((knightA[0], knightA[1]))
    s2.add((knightB[0], knightB[1]))
    possibleMoves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

    def makeTurn(s):
        newSet = set()
        for point in s:
            for move in possibleMoves:
                newSet.add((point[0] + move[0], point[1] + move[1]))
        return newSet
    
    while True:
        if len(s1 & s2) != 0:
            return moves
        moves += 1
        s1 = makeTurn(s1)
        if len(s1 & s2) != 0:
            return moves
        s2 = makeTurn(s2)


tests = [
    {
        "1": [0, 0],
        "2": [0, 0],
        "expected": 0
    },
    {
        "1": [20, 20],
        "2": [0, 0],
        "expected": 7
    },
    {
        "1": [0, 0],
        "2": [-1, -1],
        "expected": 1
    }
]


for t in tests:
    res = knightConnection(t["1"], t["2"])
    if res != t["expected"]:
        print("result: ", res, ", expected: ", t["expected"])
    else:
        print("Ok")