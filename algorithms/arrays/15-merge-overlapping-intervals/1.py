# TC O(N log N)
# SC O(N)

def mergeOverlappingIntervals(intervals):
    res = []
    intervals.sort()
    
    minNum, maxNum = intervals[0]
    
    for i in range(1, len(intervals)):
        if maxNum < intervals[i][0]:
            res.append([minNum, maxNum])
            minNum, maxNum = intervals[i]
        maxNum = max(intervals[i][1], maxNum)
    res.append([minNum, maxNum])
    return res


tests = [
    {
        "intervals": [
            [43, 49],
            [9, 12],
            [12, 54],
            [45, 90],
            [91, 93]
        ],
        "expected": [[9, 90], [91, 93]]
    },
    {"intervals": [[0, 0]], "expected": [[0, 0]]},
    {"intervals": [[1, 7], [7, 8]], "expected": [[1, 8]]},
    {"intervals": [[1, 8], [2, 9]], "expected": [[1, 9]]},
    {"intervals": [[1, 3], [5, 5], [4, 6]], "expected": [[1, 3], [4, 6]]},
    {"intervals": [
        [1, 2],
        [3, 5],
        [4, 7],
        [6, 8],
        [9, 10]
    ], "expected": [
        [1, 2],
        [3, 8],
        [9, 10]
    ]},
    {"intervals": [[1, 8], [2, 9]], "expected": [[1, 9]]},
    {
        "intervals": [
            [89, 90],
            [-10, 20],
            [-50, 0],
            [70, 90],
            [90, 91],
            [90, 95]
        ],
        "expected": [
            [-50, 20],
            [70, 95]
        ]
    }
]

for t in tests:
    res = mergeOverlappingIntervals(t["intervals"])
    if res != t["expected"]:
        print(f"reseived: {res} when {t["expected"]} expected")
    else:
        print("OK")