# 1. Most frequent item in list (easy)
#     ["a", "b", "a", "c", "b", "a"]
#
#     "a"

from collections import Counter

def get_most_common(chars):
    return Counter(chars).most_common(1)[0][0]


def run_tests():
    tests = [{
        "payload": ["a", "b", "a", "c", "b", "a"],
        "expected": "a"
    }]

    for idx, t in enumerate(tests):
        result = get_most_common(t["payload"])
        print(f"Test: {idx + 1}")
        if result == t["expected"]:
            print("OK")
        else:
            print(f"Received \"{result}\" when \"{t["expected"]}\" expected")

run_tests()