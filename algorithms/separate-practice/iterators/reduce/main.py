from functools import reduce

# ✅ Easy — Product of all numbers
#     📋 Given a list of integers, return the product of all numbers using reduce.
#     [2, 3, 4]
#     → 24

def multiply_all(nums):
    return reduce(lambda acc, n: acc * n, nums)

print(multiply_all([2, 3, 4]) == 24)


# 🟡 Medium — Longest string in list
#     📋 Given a list of strings, return the longest one using reduce.
#     ["cat", "elephant", "dog", "hippopotamus"]
#     → "hippopotamus"

def get_longest(words):
    return reduce(lambda acc, w: w if len(w) > len(acc) else acc, words)

print(get_longest(["cat", "elephant", "dog", "hippopotamus"]) == "hippopotamus")
