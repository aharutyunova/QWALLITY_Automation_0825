'''
1.	Write a Python program to get the Fibonacci series between 0 to 50.
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 0 1 1 2 3 5 8 13 21 34

'''

# Initilaize two variables
a, b = 0, 1

# Define the maximum limit
max_limit = int(input("Input your number: "))

print(a, end=' ')
while b <= max_limit:
    print(b, end=' ')
    a, b = b, a + b



'''2.	Write a Python program that accepts a string and calculate the number of digits and letters.  
Sample Data: Python 3.11
Expected Output:
Letters 6
Digits 2
'''

# Input the string
input_string = 'Python 3.11'

# Initialize counts for letters and digits
letter_count = 0
digit_count = 0

# Iterate through each character in the input string
for i in input_string:
    if i.isalpha():
        letter_count += 1
    elif i.isdigit():
        digit_count += 1
    else:
        continue

# Print the results
print("Letters", letter_count)
print("Digits", digit_count)


'''
3.	Write a Python program to print alphabet pattern 'L'
Expected Output:
*                                                                      
*                                                                      
*                                                                      
*                                                                      
*                                                                      
*                                                                      
*****
'''
# Define the height of the 'L' shape
length = 6

# Iterate through each row
for i in range(length):
    if i == length - 1:
        print('*' * length)  # Print the base of the "L"
    else:
        print('*')  # Print the vertical line of the "L"

'''
4.	Write a Python program that reads two integers representing a month and day 
and prints the season for that month and day.

Expected Output:
Month: July(7)
Day: 31
Season: Summer
'''
seasons = {
    12: "Winter",
    1: "Winter",
    2: "Winter",
    3: "Spring",
    4: "Spring",
    5: "Spring",
    6: "Summer",
    7: "Summer",
    8: "Summer",
    9: "Autumn",
    10: "Autumn",
    11: "Autumn"
}

month_input = input("Please, enter Month (1-12): ")
day_input = input("Please, enter Day (1-31): ")

if month_input.isdigit() and day_input.isdigit():
    month = int(month_input)
    day = int(day_input)
    if 1 <= month <= 12:
        if 1 <= day <= 31:
            if (month in (1, 3, 5, 7, 8, 10, 12) and day <= 31) or \
               (month in (4, 6, 9, 11) and day <= 30) or \
               (month == 2 and day <= 29):
                season = seasons[month]
                print(f"Season: {season}")
            else:
                print("Invalid Input: The day is not valid for the selected month.")
        else:
            print("Invalid Input: The day is out of range (1-31).")
    else:
        print("Invalid Input: The entered month is out of range (1-12).")
else:
    print("Invalid Input: Please enter valid numeric values for month and day.")


"""
5.	Write a Python program to find the median of few values. 
Expected Output:
numbers: 15, 26, 28, 33   or   1, 4, 5, 6, 7

"""
# List of numbers
num_list = [1, 8, 7, 5, 7, 5]
num_list.sort()

# Finding the median
n = len(num_list)
mid = n // 2

if n % 2 == 0:
    median = (num_list[mid - 1] + num_list[mid]) / 2
else:
    median = num_list[mid]

print(f"Median = {median}")
