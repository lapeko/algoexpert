from collections import deque

def get_first_positive_in_windows(nums, window_size):
    if not 1 <= window_size <= len(nums):
        raise ValueError("Provided args error. Args condition should met: 1 <= window_size <= len(nums)")

    que = deque()
    result = []

    for idx in range(len(nums)):
        if que and que[0] <= idx - window_size:
            que.popleft()
        if nums[idx] >= 0:
            que.append(idx)
        if idx >= window_size -1:
            result.append(nums[que[0]] if len(que) else 0)

    return result

def run_tests():
    tests = [{
        "payload": {
            "nums": [12, -1, -7, 8, 15, 30, 16, 28],
            "size": 3
        },
        "expected": [12, 8, 8, 8, 15, 30]
    }]

    for idx, t in enumerate(tests):
        payload = t["payload"]
        result = get_first_positive_in_windows(payload["nums"], payload["size"])
        print(f"Test {idx + 1}")
        if not result == t["expected"]:
            print(f"Received {result} when {t["expected"]} was expected")
        else:
            print("OK")
        print()

run_tests()