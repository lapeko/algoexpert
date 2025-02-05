def nonConstructibleChange(coins):
    coins.sort()
    minChange = 1
    for coin in coins:
        if coin <= minChange:
            minChange += coin
    
    return minChange



tests = [
    {
        "array": [5, 7, 1, 1, 2, 3, 22],
        "expected": 20
    },
]


for t in tests:
    res = nonConstructibleChange(t["array"])
    if res != t["expected"]:
        print("result: ", res, ", expected: ", t["expected"])
    else:
        print("Ok")