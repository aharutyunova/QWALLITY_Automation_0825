"""Exercises regarding number and string
1.	Write a Python program to calculate the length of a string.
my_string = 'Here is string for your exercise!'

2.	Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
Sample String : 'w3resource'
Expected Result : 'w3ce'

3.	Write a Python program to replace 'cut' word to 'dog'
Sample String : 'I have a cut and I love it'
Expected Result : 'I have a dog and I love it'

4.	Write a Python program to reverse 123  to 321 in text.
Sample String : 'I have 123 books'
Expected Result : 'I have 321 books'

5.	Replace all occurrence of word five to one.
Sample String : "five five was a race horse, two two was one too."
Expected Result "one one was a race horse, two two was one too."


6.	Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False

7.	Write a Python program to solve (x + y) * (x + y). 
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49

8.	Write a Python program which converts float values to integer, and sum of two values, then result print with reversed order.
Test Data: x = 2,5 , y = 13.75
Expected Output: 51


"""

# 1. Calculate the length of a string
my_string = 'Here is string for your exercise!'
print("1. Length of string:", len(my_string))


# 2. Get a string made of the first 2 and the last 2 chars
sample_str = 'w3resource'
b = sample_str[0:2]
c = sample_str[-2:]
result = "".join([b, c])
print("2.", result)

# 3. Replace 'cut' word with 'dog'
sample_str = 'I have a cut and I love it'
result = sample_str.replace('cut', 'dog')
print("3. Result:", result)


# 4. Reverse 123 to 321 in text
sample_str = "I have 123 books"
number = "123"
reversed_number = "".join(reversed(number))
result = sample_str.replace(number, reversed_number)
print("4.", result)

# 5. Replace all occurrences of 'five' with 'one'
sample_str = "five five was a race horse, two two was one too."
result = sample_str.replace('five', 'one')
print("5. Result:", result)


# 6. Check whether a specified value is contained in a group of values
def check_value(value, group):
    return value in group


print("6.", check_value(3, [1, 5, 8, 3]))
print("6.", check_value(-1, [1, 5, 8, 3]))


# 7. Solve (x + y) * (x + y)
x, y = 4, 3
result = (x + y) * (x + y)
print(f"7. ({x} + {y}) ^ 2 = {result}")


# # 8. Convert float values to integer, sum them, then reverse result
x, y = 2.5, 13.75
x_int, y_int = int(x), int(y)
total = x_int + y_int
reversed_result = "".join(reversed(str(total)))
print("8. Result:", reversed_result)
