# unordered list unique ints
# range [1, n]
# two numbers missed in the list

# TC O(N)
# SC O(N)

def missingNumbers(nums):
    result = []
    wholeLength = len(nums) + 2

    numSet = set(nums)

    for num in range(1, wholeLength + 1):
        if num not in numSet:
            result.append(num)

    return result


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