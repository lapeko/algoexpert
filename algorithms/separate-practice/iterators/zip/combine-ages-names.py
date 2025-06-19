# ✅ 1. Easy — Combine names and ages
#     📋 Given two lists, one of names and one of ages, return a list of strings like "Alice is 30".
#     ["Alice", "Bob"], [30, 25]
#     → ["Alice is 30", "Bob is 25"]

def combine_names_with_ages(names, ages):
    return [f"{name} is {age}" for name, age in zip(names, ages)]

print(combine_names_with_ages(["Alice", "Bob"], [30, 25]) == ["Alice is 30", "Bob is 25"])

# 🟡 2. Medium — Transpose a matrix
#     📋 Given a 2D list (matrix), return its transpose using zip().
#     [
#         [1, 2, 3],
#         [4, 5, 6]
#     ]
#     → [
#         [1, 4],
#         [2, 5],
#         [3, 6]
#     ]

def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

print(transpose_matrix([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]])