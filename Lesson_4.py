"""Exercises regarding number and string
1.	Write a Python program to calculate the length of a string."""
my_string = 'Here is string for your exercise!'
print(len(my_string))

"""2.	Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
Sample String : 'w3resource'
Expected Result : 'w3ce'"""
Sample_String = "w3resource"
x = Sample_String[0:2]
y = Sample_String[-2:]
new_Sample_String = x + y
print(new_Sample_String)

"""3.	Write a Python program to replace 'cut' word to 'dog'
Sample String : 'I have a cut and I love it'
Expected Result : 'I have a dog and I love it'"""
Sample_String1 = 'I have a cut and I love it'
new_Sample_String1 = Sample_String1.replace('cut', 'dog')
print(new_Sample_String1)


"""4.	Write a Python program to reverse 123  to 321 in text.
Sample String : 'I have 123 books'
Expected Result : 'I have 321 books'"""
Sample_String2 = 'I have 123 books'
number = '123'
reversed_number = ''.join(reversed(number))
new_Sample_String2 = Sample_String2.replace(number, reversed_number)
print(new_Sample_String2)

"""5.	Replace all occurrence of word five to one.
Sample String : "five five was a race horse, two two was one too."
Expected Result "one one was a race horse, two two was one too."""
Sample_String3 = "five five was a race horse, two two was one too."
word_replace = Sample_String3.replace('five', 'one')
print(word_replace)


"""6.	Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False"""
list = [1, 5, 8, 3] 
print(3 in list)
print(-1 in list)


"""7.	Write a Python program to solve (x + y) * (x + y). 
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49"""
x = 4
y = 3
output = (x+y)**2
print(output)

"""8.	Write a Python program which converts float values to integer, and sum of two values, then result print with reversed order.
Test Data: x = 2,5 , y = 13.75
Expected Output: 51
"""
x = 2.5
y = 13.75
sum = str(int(x) + int(y))
print(sum)
reversed_num = int("".join(reversed(sum)))
print(reversed_num)

# Anna - everything is correct, good job!!!