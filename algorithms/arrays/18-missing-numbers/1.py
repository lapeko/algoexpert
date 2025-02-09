# unordered list unique ints
# range [1, n]
# two numbers missed in the list

# TC O(N)
# SC O(1)

from math import sqrt

def missingNumbers(nums):
    wholeLength = len(nums) + 2
    wholeSum = int((1 + wholeLength) * wholeLength / 2)
    wholeSquaredSum = sum(i * i for i in range(1, wholeLength + 1))
    missedSum = wholeSum
    missedSquaredSum = wholeSquaredSum

    for num in nums:
        missedSum -= num
        missedSquaredSum -= num ** 2

    # missedSum = x + y
    # x = missedSum - y
    # missedSquaredSum = x^2 + y^2
    # missedSquaredSum = (missedSum - y)^2 + y^2
    # missedSquaredSum = missedSum^2 - 2*missedSum*y + y^2 + y^2
    # 2*y^2 - 2*missedSum*y + missedSum^2 - missedSquaredSum

    # D = b^2 - 4*a*c
    # x1, x2 = -b +- sqrt(D) / 2a

    # D = (2*missedSum)^2 - 8 * (missedSum^2 - missedSquaredSum)
    # D = 4*missedSum^2 - 8*missedSum^2 + 8*missedSquaredSum
    # D = 8*missedSquaredSum - 4*missedSum^2
    # x1 = (2*missedSum - sqrt(8*missedSquaredSum - 4*missedSum^2)) / 4
    # x2 = (2*missedSum + sqrt(8*missedSquaredSum - 4*missedSum^2)) / 4

    D = 8 * missedSquaredSum - 4 * missedSum ** 2
    x1 = int((2 * missedSum - sqrt(D)) / 4)
    x2 = int((2 * missedSum + sqrt(D)) / 4)

    return [x1, x2]


tests = [
    {
        "nums": [],
        "expected": [1, 2]
    },
        {
        "nums": [4, 1],
        "expected": [2, 3]
    },
        {
        "nums": [4, 1, 3],
        "expected": [2, 5]
    },
    {
        "nums": [2],
        "expected": [1, 3]
    },
    {
        "nums": [2, 1, 5],
        "expected": [3, 4]
    },
    {
        "nums": [2, 1, 3, 10, 7, 6, 8, 9, 11],
        "expected": [4, 5]
    }
]

for t in tests:
    res = missingNumbers(t['nums'])
    if res != t["expected"]:
        print(f"received: {res}\nexpected: {t["expected"]}")
    else:
        print("OK")