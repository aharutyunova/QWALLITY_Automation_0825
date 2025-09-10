"""Exercises regarding number and string
1.	Write a Python program to calculate the length of a string. """

my_string = 'Here is string for your exercise!'
print("Exercise_1")
print(len(my_string))

"""2.	Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
Sample String : 'w3resource'
Expected Result : 'w3ce' """

sample_string = 'w3resource'
new_string = sample_string[0:2] + sample_string[-2:] #TODO You could also write sample_string[:2] + sample_string[-2:]
print("Exercise_2")
print(new_string)

"""3.	Write a Python program to replace 'cut' word to 'dog'
Sample String : 'I have a cut and I love it'
Expected Result : 'I have a dog and I love it' """

old_string = 'I have a cut and I love it'
replaced_string = old_string.replace("cut", "dog")
print("Exercise_3")
print(replaced_string)

"""4.	Write a Python program to reverse 123  to 321 in text.
Sample String : 'I have 123 books'
Expected Result : 'I have 321 books' """

reversed_string = "".join(reversed("123"))
first_string = 'I have 123 books'
new_string = first_string.replace("123", reversed_string)
print("Exercise_4")
print(new_string)


"""5.	Replace all occurrence of word five to one.
Sample String : "five five was a race horse, two two was one too."
Expected Result "one one was a race horse, two two was one too." """

given_string = "five five was a race horse, two two was one too."
expected_string = given_string.replace("five", "one")
print("Exercise_5")
print(expected_string)


"""6.	Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False """

test_data = [1, 5, 8, 3]
print("Exercise_6")
print(3 in test_data)
print(-1 in test_data)

"""7.	Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49 """

x = 4
y = 3
z = (x + y) ** 2
print("Exercise_7")
print(z)

"""8.	Write a Python program which converts float values to integer, and sum of two values, then result print
with reversed order.
Test Data: x = 2,5 , y = 13.75
Expected Output: 51"""

x = 2.5
y = 13.75
a = int(x) + int(y)
print("Exercise_8")
print("".join(reversed(str(a))))

# Good Job!!!