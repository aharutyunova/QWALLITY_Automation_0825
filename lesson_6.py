"""
1. Write a Python program to get the Fibonacci series between 0 and 50.
Note : The Fibonacci Sequence is the series of numbers : 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 0 1 1 2 3 5 8 13 21 34
"""
first_number = 0
second_number = 1
print("Fibonacci series between 0 and 50:")

while first_number <= 50:
    print(first_number, end=" ")
    first_number, second_number = second_number, first_number + second_number

print()

"""
2. Write a Python program that accepts a string and calculate the number of digits and letters.
  Sample Data: Python 3.13
  Expected Output: Letters 6
  Digits 3
"""
digit_count = 0
letter_count = 0
given_test = input("Input a text: ")
for letter in given_test:
    if letter.isdigit():
        digit_count += 1
    elif letter.isalpha():
        letter_count += 1
    else:
        continue

print("Letters: ", letter_count)
print("Digits: ", digit_count)

"""3. Write a Python program to print alphabet pattern 'L'
Expected Output:
*
*
*
*
*
*
*****
"""

given_data = [1, 1, 1, 1, 1, 1, 2]
for i in given_data:
    if i == 1:
        print("*", end="\n")
    if i == 2:
        print("*****", end="\n")
    else:
        continue

"""
4. Write a Python program that reads two integers representing a month and day and prints the season for that month
and day.
Expected Output:
Month: July(7)
Day: 31
Season: Summer
"""
input_month = int(input("Input a month: "))
input_day = int(input("Input a day: "))
month_list = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July",
              8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
days_in_month = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

if input_month not in month_list:
    print("Invalid month")
else:
    if input_day < 1 or input_day > days_in_month[input_month]:
        print(f"Invalid day for {month_list[input_month]}")
    else:
        if input_month == 12 or input_month in [1, 2]:
            season = "Winter"
        if input_month in [3, 5]:
            season = "Spring"
        if input_month in [6, 8]:
            season = "Summer"
        else:
            season = "Autumn"
        print(f"Month: {month_list[input_month]}({input_month})")
        print(f"Day: {input_day}")
        print(f"Season: {season}")

"""
5. Write a Python program to find the median of few values.
Expected Output:
numbers: 15, 26, 28, 33   or   1, 4, 5, 6, 7
"""
numbers = [15, 26, 28, 33, 3]
numbers.sort()
n = len(numbers)
mid = n // 2

if n % 2 == 0:
    median = int(numbers[mid - 1] + numbers[mid]) / 2
    print("The median is ", median)
else:
    median = int(numbers[mid])
    print("The median is ", median)









