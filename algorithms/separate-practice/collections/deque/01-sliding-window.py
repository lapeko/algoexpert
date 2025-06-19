from collections import deque

# def get_max_item_in_window(nums, k):
#     if k < 1:
#         raise "Window size should be a positive number between 1 and size of the provided nums [1, len(nums)]"
#     steps_num = len(nums) - k + 1
#     if steps_num < 1:
#         raise "Provided size of list should be equal or higher the size of window k"
#
#     result = []
#     for i in range(steps_num):
#         queue = deque(nums[i:k + i])
#         result.append(max(queue))
#
#     return result


def get_max_item_in_window(nums, k):
    if not 1 <= k <= len(nums):
        raise ValueError("Window size k should be between 1 and len(nums) [1, len(nums)]")

    result = []
    que = deque()

    for idx in range(len(nums)):
        while que:
            if que[0] <= idx - k:
                que.popleft()
            elif nums[que[-1]] <= nums[idx]:
                que.pop()
            else:
                break
        que.append(idx)
        if idx >= k - 1:
            result.append(nums[que[0]])

    return result


def run_tests():
    tests = [{
        "payload": {
            "nums": [1, 3, -1, -3, 5, 3, 6, 7],
            "size": 3
        },
        "expected": [3, 3, 5, 5, 6, 7]
    }]

    for idx, t in enumerate(tests):
        payload = t["payload"]
        result = get_max_item_in_window(payload["nums"], payload["size"])
        print(f"Test {idx + 1}")
        if not result == t["expected"]:
            print(f"Received {result} when {t["expected"]} was expected")
        else:
            print("OK")
        print()

run_tests()