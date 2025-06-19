# 🔹 1. Most frequent word in a list (easy)
#     You’re given a list of strings. Return the most frequent word.
#     ["apple", "banana", "apple", "orange", "banana", "apple"]
#     → "apple"

from collections import Counter

def get_most_frequent_word(words):
    if not words:
        return ""
    res = Counter(words)
    return max(res, key=res.get)

print(get_most_frequent_word(["apple", "banana", "apple", "orange", "banana", "apple"]) == "apple")
print(get_most_frequent_word(["a", "b"]) == "a")
print(get_most_frequent_word([]) == "")