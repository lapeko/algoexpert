def insertion_sort(array):
    arr = array.copy()
    for idx in range(1, len(arr)):
        for left in range(idx - 1, -1, -1):
            right = left + 1
            if not arr[right] < arr[left]:
                break
            arr[left], arr[right] = arr[right], arr[left]
    return arr

tests = [
    {
        "array": [8, 5, 2, 9, 5, 6, 3],
        "expected": [2, 3, 5, 5, 6, 8, 9]
    },
    {
        "array": [1],
        "expected": [1]
    },
    {
        "array": [1, 2],
        "expected": [1, 2]
    },
    {
        "array": [2, 1],
        "expected": [1, 2]
    },
    {
        "array": [1, 3, 2],
        "expected": [1, 2, 3]
    },
    {
        "array": [],
        "expected": []
    }
]

for t in tests:
    res = insertion_sort(t['array'])
    expectation = t['expected']
    if not res == expectation:
        print(f"Result is: {res}, when expected: {expectation}")
    else:
        print('Ok')