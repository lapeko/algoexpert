def sweetAndSavory(dishes, target):
    result = [0, 0]
    dishes.sort()
    left, right = 0, len(dishes) - 1
    bestFlawor = float("-inf")
    while left < right and dishes[left] < 0 and dishes[right] > 0:
        if dishes[left] + dishes[right] > target:
            right -= 1
        else:
            if bestFlawor < dishes[left] + dishes[right]:
                bestFlawor = dishes[left] + dishes[right]
                result = [dishes[left], dishes[right]]
            left += 1
    return result
            

        




tests = [
    {
        "1": [],
        "2": 10,
        "expected": [0, 0]
    },
    {
        "1": [4],
        "2": -10,
        "expected": [0, 0]
    },
    {     
        "1": [-5, 10],
        "2": 5,
        "expected": [-5, 10]
    },
    {
        "1": [-3, -5, 1, 7],
        "2": 8,
        "expected": [-3, 7]
    }
]


for t in tests:
    res = sweetAndSavory(t["1"], t["2"])
    if res != t["expected"]:
        print("result: ", res, ", expected: ", t["expected"])
    else:
        print("Ok")