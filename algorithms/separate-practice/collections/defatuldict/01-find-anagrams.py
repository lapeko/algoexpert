from collections import defaultdict

def find_anagrams(words):
    hashed_word_map = defaultdict(list)
    result = []
    for w in words:
        key = "".join(sorted(w))
        hashed_word_map[key].append(w)
    for v in hashed_word_map.values():
        result.append(v)
    return result


def run_tests():
    tests = [{
        "payload": ["eat", "tea", "tan", "ate", "nat", "bat"],
        "expected": [
            ["eat", "tea", "ate"],
            ["tan", "nat"],
            ["bat"]
        ],
    }]

    for idx, t in enumerate(tests):
        print(f"Test {idx + 1}")
        result = find_anagrams(t["payload"])
        if normalize_output(result) == normalize_output(t["expected"]):
            print("OK")
        else:
            print(f"Received {result} when {t["expected"]} was expected")


def normalize_output(output):
    return sorted(sorted(group) for group in output)


run_tests()