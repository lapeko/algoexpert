# ✅ Easy — Sort by second element
#     📋 Given a list of tuples, sort them by the second element.
#     [(1, 3), (2, 1), (4, 2)]
#     → [(2, 1), (4, 2), (1, 3)]

def sort_by_second(matrix):
    return sorted(matrix, key=lambda tpl: tpl[1])

print(sort_by_second([(1, 3), (2, 1), (4, 2)]) == [(2, 1), (4, 2), (1, 3)])

# 🟡 Medium — Sort by last character of string
#     📋 Given a list of strings, sort them by their last character.
#     ["cat", "dog", "apple"]
#     → ["apple", "dog", "cat"]

def sort_by_last_char(words):
    return sorted(words, key=lambda w: w[-1])

print(sort_by_last_char(["cat", "dog", "apple"]) == ["apple", "dog", "cat"])
