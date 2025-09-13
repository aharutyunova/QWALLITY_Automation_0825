# 1.Write a Python program to calculate the length of a string.
my_string = "Here is string for your exercise!"


print(len(my_string))

# 2.	Write a Python program to get a string made of the first 2 and the last 2 
# chars from a given a string.
random_string = "w3resource"
first_and_last_two = random_string[0:2] + random_string[-2:]


print(first_and_last_two)

# 3.Write a Python program to replace 'cut' word to 'dog'
# Sample String : 'I have a cut and I love it'
# Expected Result : 'I have a dog and I love it'

Initial_string = 'I have a cut and I love it'
replaced_string = Initial_string.replace('cut', 'dog')

print(replaced_string)

""" 4.Write a Python program to reverse 123  to 321 in text.
Sample String : 'I have 123 books'
Expected Result : 'I have 321 books'"""

text = 'I have 123 books'
replaced_text = text.replace("123", "321")


print(replaced_text)

""" 5.Replace all occurrence of word five to one.
Sample String : "five five was a race horse, two two was one too."
Expected Result "one one was a race horse, two two was one too."""


numbers_string = "five five was a race horse, two two was one too."
replaced_numbers_string = numbers_string.replace("five", "one")


print(replaced_numbers_string)

""" 6.Write a Python program to check whether a
 specified value is contained in a group of values."""

test_list = [1, 5, 8, 3]
number = int(input("Input Your Number: "))
is_in_list = None


if number in test_list:
    is_in_list = True
else:
    is_in_list = False

print(is_in_list)

# 7.Write a Python program to solve (x + y) * (x + y). 

first_number = 4
second_number = 3

sum = first_number + second_number
simple_arithmetic_operation = sum ** 2


print(simple_arithmetic_operation)

print("(", first_number, "+", second_number, ")", "^ 2", "=", 
      simple_arithmetic_operation)

""" 8.Write a Python program which converts float values to integer,
 and sum of two values, then result print with reversed order."""

first_float_number = float(input("Input your first number: "))
second_float_number = float(input("Input your second number: "))

first_int_number = int(first_float_number)
second_int_number = int(second_float_number)

sum_of_two = (first_int_number + second_int_number)

reversed_sum = str(sum_of_two)[::-1]

print(reversed_sum)

# Good Job!!!