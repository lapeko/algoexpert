def subarraySort(array):
    startIdx, endIdx = -1, -1
    smallestOutOfOrder = float("inf")
    largestOutOfOrder = float("-inf")
    for idx in range(1, len(array)):
        if array[idx - 1] > array[idx] and smallestOutOfOrder > array[idx]:
            smallestOutOfOrder = array[idx]
    
    for idx in range(len(array) - 1, 0, -1):
        if array[idx - 1] > array[idx] and largestOutOfOrder < array[idx - 1]:
            largestOutOfOrder = array[idx - 1]
    
    for idx, num in enumerate(array):
        if num > smallestOutOfOrder:
            startIdx = idx
            break
    
    for idx in range(len(array) - 1, -1, -1):
        if array[idx] < largestOutOfOrder:
            endIdx = idx
            break

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