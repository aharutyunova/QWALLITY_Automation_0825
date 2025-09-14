# 1.	Write a Python program to get the Fibonacci series between 0 to 50.
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 0 1 1 2 3 5 8 13 21 34
# numbers = [0, 1]
# while True:
#     next_number = numbers[-1] + numbers[-2]
#     if next_number > 50:
#         break
#     numbers.append(next_number)
# print("Fibonacci series up to 50:", numbers)

# Anna - Correct

# 2.	Write a Python program that accepts a string and calculate the
# number of digits and letters.
# Sample Data: Python 3.13
# Expected Output:
# Letters 6
# Digits 3
# new_text = input("Please input a text: ")

# sum_of_letters = 0
# sum_of_digits = 0

# for i in new_text:
#     if i.isdigit():
#         sum_of_digits += 1
#     elif i.isalpha():
#         sum_of_letters += 1

# print("Letters", sum_of_letters)
# print("Digits", sum_of_digits)

# Anna - Correct

# 3.	Write a Python program to print alphabet pattern 'L'
# Expected Output:
# *                                                                    
# *                                                                    
# *                                                                     
# *                                                                      
# *                                                                      
# *                                                                      
# *****
rows = 7
cols = 5

# for i in range(rows):
#     for j in range(cols):
#         if j == 0 or (i == rows - 1):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# TODO The result is correct, but the solution is not very efficient since it uses an unnecessary inner loop.
# You could just have the same result with 1 loop

for i in range(rows):
    if i == rows - 1:
        print("*" * cols)
    else:
        print("*")

# 4.	Write a Python program that reads two integers representing a month and
#  day and prints the season for that month and day.
# Expected Output:
# Month: July(7)          
# Day: 31
# Season: Summer                                                 
# month = int(input("Please enter a month"))
# day = int(input("Please enter a day"))
# season = ""

# if (month == 12 and day >= 21) or \
#       (month in [1, 2]) or (month == 3 and day <= 19):
#     season = "Winter"
# elif (month == 3 and day >= 20) or \
#       (month in [4, 5]) or (month == 6 and day <= 20):
#     season = "Spring"
# elif (month == 6 and day >= 21) or \
#      (month in [7, 8]) or (month == 9 and day <= 22):
#     season = "Summer"
# elif (month == 9 and day >= 23) or \
#      (month in [10, 11]) or (month == 12 and day <= 20):
#     season = "Autumn"

# print("Month:", month)
# print("Day:", day)
# print("Season:", season)

# TODO: Generally correct. You just didn’t handle exceptional cases, for example, an incorrect day or month.

# 5.	Write a Python program to find the median of few values.
# Expected Output:
# numbers: 15, 26, 28, 33   or   1, 4, 5, 6, 7                                               
# median calculation example:
numbers = [15, 10, 20, 33, 50]
n = len(numbers)
median = 0
if n % 2 == 0:
    median = (numbers[n//2 - 1] + numbers[n//2]) / 2
else:
    median = numbers[n//2]

print("Median:", median)

# Anna - Correct

# Good Job!!!