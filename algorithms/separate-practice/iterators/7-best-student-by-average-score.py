from statistics import mean

# 🔹 7. Return student with highest average score (medium)
#     Given a list of students, where each student is a tuple of name and list of scores, return the student with the highest average score.
#     [
#         ("Alice", [80, 90, 70]),
#         ("Bob", [100, 50]),
#         ("Charlie", [90, 90, 90])
#     ]
#     → "Charlie"


def get_best_student_by_average_score(students_data):
    return max(students_data, key=lambda sd: mean(sd[1]))[0]

print(get_best_student_by_average_score([("Alice", [80, 90, 70]), ("Bob", [100, 50]), ("Charlie", [90, 90, 90])]) == "Charlie")