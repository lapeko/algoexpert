def minRewards(scores):
    awardsArr = [1] * len(scores)
    for i in range(len(scores) - 1):
        if scores[i + 1] > scores[i]:
            awardsArr[i + 1] = awardsArr[i] + 1
    for i in range(len(scores) - 1, 0, -1):
        if scores[i - 1] > scores[i]:
            awardsArr[i - 1] = max(awardsArr[i - 1], awardsArr[i] + 1)
    return sum(awardsArr)
    


tests = [
    {
        "1": [8, 4, 2, 1, 3, 6, 7, 9, 5],
        "expected": 25
    },
    {
        "1": [1],
        "expected": 1
    },
    {     
        "1": [2, 1, 4, 3, 6, 5, 8, 7, 10, 9],
        "expected": 15
    },
    {
        #     1  2                        1  2  3  4  5   
        #        8   7   6   5   4  3  2  1           2  1
        #     0  7   6   5   4   3  2  1  0  1  2  3  4  0
        #     1  8   7   6   5   4  3  2  1  2  3  4  5  1
        "1": [2, 20, 13, 12, 11, 8, 4, 3, 1, 5, 6, 7, 9, 0],
        "expected": 52
    }
]


for t in tests:
    res = minRewards(t["1"])
    if res != t["expected"]:
        print("result: ", res, ", expected: ", t["expected"])
    else:
        print("Ok")