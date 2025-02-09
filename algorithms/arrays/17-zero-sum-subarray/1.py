# TC O(N^3)
# SC O(1)

def zeroSumSubarray(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if sum(nums[i] for i in range(i, j + 1)) == 0:
                return True
    return False


tests = [
    {"nums": [], "expected": False},
    {"nums": [1], "expected": False},
    {"nums": [0], "expected": True},
    {"nums": [2, 5], "expected": False},
    {"nums": [3, 5, -9, 1], "expected": True},
    {"nums": [1, 2, 3, 0, 5], "expected": True},
    {"nums": [-5, 6, -20, 1, -1, 1, 18], "expected": True},
]

for t in tests:
    result = zeroSumSubarray(t["nums"])
    if result != t["expected"]:
        print(f"Expected: {t['expected']}. Received: {result}")
    else:
        print("OK")