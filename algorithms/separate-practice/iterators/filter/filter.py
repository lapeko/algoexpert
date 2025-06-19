# ✅ Easy — Keep positive numbers only
#     📋 Given a list of numbers, return a list of only positive numbers.
#     [-3, 0, 2, -5, 4]
#     → [2, 4]

def filter_positives(nums):
    return list(filter(lambda x: x > 0, nums))

print(filter_positives([-3, 0, 2, -5, 4]) == [2, 4])

# 🟡 Medium — Filter words starting with vowel
#     📋 Given a list of words, return only those that start with a vowel.
#     ["apple", "banana", "orange", "grape"]
#     → ["apple", "orange"]

def filter_starting_with_vowel(words):
    vowels = {"a", "e", "i", "o", "u"}
    return list(filter(lambda w: w[0].lower() in vowels, words))

print(filter_starting_with_vowel(["apple", "banana", "orange", "grape"]) == ["apple", "orange"])