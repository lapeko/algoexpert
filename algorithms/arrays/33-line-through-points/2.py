from collections import defaultdict

def get_direction(p1, p2):
    d_y = p1[1] - p2[1]
    return abs((p1[0] - p2[0]) / d_y) if not d_y == 0 else float("inf")

def lineThroughPoints(points):
    line_direction_points_set = defaultdict(int)
    for idx, p1 in enumerate(points):
        for p2 in points[idx:]:
            bottom_left = tuple(sorted([p1, p2], key=lambda p: (p[0], p[1]))[0])
            direction = get_direction(p1, p2)
            key = f"{bottom_left}{direction}"
            value = line_direction_points_set[key]
            line_direction_points_set[key] = 2 if not value else value + 1
    print(line_direction_points_set)
    return max(line_direction_points_set.values())


tests = [
    {
        "array": [
            [1, 1],
            [2, 2],
            [3, 3],
            [0, 4],
            [-2, 6],
            [4, 0],
            [2, 1]
        ],
        "expected": 4
    },
    {
        "array": [
            [1, 1],
        ],
        "expected": 1
    },
    {
        "array": [
            [-1, -1],
            [-3, -1],
            [-4, -1],
            [1, 1],
            [4, 1]
        ],
        "expected": 3
    },
]



for t in tests:
    res = lineThroughPoints(t["array"])
    if res != t["expected"]:
        print("result: ", res, ", expected: ", t["expected"])
    else:
        print("Ok")