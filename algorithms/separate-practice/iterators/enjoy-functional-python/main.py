from functools import reduce, partial
from collections import Counter
from itertools import groupby
from re import findall


# ✅ 1. Check if all users are adults (lambda + all + map)
# 🧾 Given a list of dicts like {"name": "Alice", "age": 25}, check if all users are at least 18 years old.

def check_all_adults(people):
    return all(map(lambda p: p["age"] >= 18, people))

print(check_all_adults([{"name": "Alice", "age": 25}]) == True)


# ✅ 2. Get total price with tax applied only to certain products (map + filter + reduce)
# 🧾 Given a list of {"name": ..., "price": ..., "taxable": True/False},
# calculate total cost including tax (assume 10%) only for taxable items.

def get_total_price(products):
    return reduce(
        lambda a, b: a + b,
        map(
            lambda p: p["price"] * (100 + 10) / 100,
            filter(lambda p: p["taxable"], products),
        )
    )

print(get_total_price([
    {"name": "melon", "price": 10, "taxable": True},
    {"name": "banana", "price": 5, "taxable": False},
    {"name": "grapes", "price": 20, "taxable": True},
]) == 33)


# ✅ 3. Find most common pair of letters (Counter + map + zip)
# 🧾 Given a list of strings, count all pairs of adjacent letters (bigrams) and return the most common one.
# (e.g. "hello" has ["he", "el", "ll", "lo"])
# Use Counter and friends. Should be implemented as case-insensitive

def find_most_common_letter_pair(word):
    w = word.lower()
    c = Counter(zip(w[:-1], w[1:]))
    return "".join(max(c, key=c.get))

print(find_most_common_letter_pair("Hello all") == "ll")


# ✅ 4. Sum of even-indexed elements > odd-indexed elements? (zip + map + reduce + all/any)
# 🧾 Given a list of integers, return True if the sum of even-indexed elements is greater than the sum of odd-indexed.

def even_sum_indexed_higher(nums):
    nums = reduce(lambda a, b: (a[0] + b[0], a[1] + b[1]), zip(nums[0::2], nums[1::2]))
    return nums[0] > nums[1]

print(even_sum_indexed_higher([1, 5, 2, 3, 3, 4]) == False)


# ✅ 5. Get top N longest words from sentence (lambda + sorted + partial + map)
# 🧾 Given a sentence string and a number N, return the top N longest words (not lengths, but actual words).
# (Use partial to predefine a custom sorting function)

def get_n_longest_words(text, n):
    sort_by_len = partial(sorted, key=len, reverse=True)
    words = findall(r"\b\w+\b", text)
    return sort_by_len(words)[:n]

print(get_n_longest_words("Hi there! How are you? Do you like nutella?", 3) == ['nutella', 'there', 'like'])


# ✅ 6. Group users by first letter of name (groupby + map + lambda + Counter)
# 🧾 Given a list of usernames, group them by the first letter, and count how many in each group.

def group_users_by_first_letter(users):
    result = {}
    for k, v in groupby(sorted(users), key=lambda w: w[0]):
        result[k] = list(v)
    return result

print(group_users_by_first_letter(["Alice", "Bob", "Adam", "Charlie", "Clara", "Brian"]) == {'A': ['Adam', 'Alice'], 'B': ['Bob', 'Brian'], 'C': ['Charlie', 'Clara']})


# ✅ 9. Build a frequency string from input (Counter + map + lambda)
# 🧾 Given a string "aabccc", return "a:2, b:1, c:3" as a single formatted string.

def get_frequency_string(text):
    return ", ".join(map(lambda i: f"{i[0]}:{i[1]}", sorted(Counter(text).items())))

print(get_frequency_string("ccccaadccb") == "a:2, b:1, c:6, d:1")