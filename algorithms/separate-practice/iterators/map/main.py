# ✅ Easy — Convert to uppercase
#     📋 Given a list of strings, return the same list with all words uppercased.
#     ["hello", "world"]
#     → ["HELLO", "WORLD"]

def convert_to_upper(words):
    return list(map(str.upper, words))

print(convert_to_upper(["hello", "world"]) == ["HELLO", "WORLD"])


# 🟡 Medium — Square all even numbers
#     📋 Given a list of numbers, square only even ones using map and lambda.
#     Odd numbers should remain unchanged.
#     [1, 2, 3, 4]
#     → [1, 4, 3, 16]

def square_even_nums(nums):
    return [n ** 2 if n % 2 == 0 else n for n in nums]

print(square_even_nums([1, 2, 3, 4]) == [1, 4, 3, 16])
