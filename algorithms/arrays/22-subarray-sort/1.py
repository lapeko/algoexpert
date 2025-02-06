def subarraySort(array):
    startIdx, endIdx = -1, -1
    smallestOutOfOrder, largestOutOfOrder = float("inf"), float("-inf")
    for idx in range(1, len(array)):
        if array[idx - 1] > array[idx]:
            smallestOutOfOrder = min(smallestOutOfOrder, array[idx])
            largestOutOfOrder = max(largestOutOfOrder, array[idx - 1])
    for idx in range(len(array)):
        if startIdx == -1 and array[idx] > smallestOutOfOrder:
            startIdx = idx
        if array[idx] < largestOutOfOrder:
            endIdx = idx
    return [startIdx, endIdx]

tests = [{
    "array": [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19],
    "expected": [3, 9],
}]


for t in tests:
    res = subarraySort(t["array"])
    if res != t["expected"]:
        print("result: ", res, ", expected: ", t["expected"])
    else:
        print("Ok")