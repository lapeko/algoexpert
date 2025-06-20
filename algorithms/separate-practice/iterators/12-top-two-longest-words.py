# 🔹 12. Top 2 longest words, alphabetically if tie (medium+)
#     Given a list of strings, return top 2 longest. If tie, break by lexicographic order.
#     ["cat", "zebra", "apple", "banana", "aardvark"]
#     → ["aardvark", "banana"]

def top_two(words):
    return sorted(words, key=lambda w: (-len(w), w))[:2]

print(top_two(["lizard", "cat", "zebra", "apple", "banana", "aardvark"]) == ["aardvark", "banana"])
