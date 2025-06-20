from functools import reduce

# 🔹 13. Most valuable word (hardish)
#     Given a dict char_scores = {"a": 1, "b": 3, "c": 5, ...} and a list of words, return the word with the highest total score.
#     words = ["abc", "bca", "aaa"]
#     → depends on scores, but e.g. "bca" if 'c' is heavy

def most_valuable(words, scores):
    def get_weight(word):
        return reduce(lambda acc, char: acc + scores[char], list(word), 0)
    return max(words, key=get_weight)

print(most_valuable(["abc", "bca", "cc", "aaaaa"], {"a": 1, "b": 3, "c": 5}) == "cc")