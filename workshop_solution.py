# 1.Input birth date in DD/MM/YYYY format and calculate age in years.

birth_date = input("Enter your birth date (DD/MM/YYYY):\n")
print(birth_date)
year = birth_date.split('/')[2]
birth_year = int(year)


current_year = 2025

age = current_year - birth_year
print(age)

# 2.You have data about students and their test scores:
# 2.1.Calculate the total score for each student and store it in a dictionary \
# where the key is the student name and the value is the total score.

# 2.2.Make a list of students who got more than 90 on at least one of their tests.

# 2.1
students_scores = {
    "Alice": (91, 92, 97),
    "Bob": (70, 88, 90),
    "Charlie": (95, 85, 100),
}

total_scores = {
    "Alice": sum(students_scores["Alice"]),
    "Bob": sum(students_scores["Bob"]),
    "Charlie": sum(students_scores["Charlie"]),
}
print(total_scores)
# 2.2
high_score_students = []
if max(students_scores["Alice"]) > 90:
    high_score_students.append("Alice")
if max(students_scores["Bob"]) > 90:
    high_score_students.append("Bob")
if max(students_scores["Charlie"]) > 90:
    high_score_students.append("Charlie")
print(high_score_students)
