def twoNumberSum(array, targetSum):
    num_set = set()
    for n in array:
        if targetSum - n in num_set:
            return [targetSum - n, n]
        num_set.add(n)
    return []

assert twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10) == [11, -1]
