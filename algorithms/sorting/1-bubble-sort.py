def bubble_sort(array):
    for left_idx in range(0, len(array) - 1):
        for right_idx in range(left_idx, len(array)):
            if array[left_idx] > array[right_idx]:
                array[left_idx], array[right_idx] = array[right_idx], array[left_idx]
    return array

tests = [
    {"array": [1, 2, 3], "expect": [1, 2, 3]},
    {"array": [2, 1], "expect": [1, 2]},
    {"array": [8, 5, 2, 9, 5, 6, 3], "expect": [2, 3, 5, 5, 6, 8, 9]}
]

for test in tests:
    res = bubble_sort(test["array"])
    if not res == test["expect"]:
        f"Received {res} when expected {test['expect']}"
    else:
        print("OK")