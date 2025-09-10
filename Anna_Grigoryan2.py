"""Exercises regarding number and string
1.	Write a Python program to calculate the length of a string."""
my_string = 'Here is string for your exercise!'
x=len(my_string)
print(x)

"""2.Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
Sample String : 'w3resource'
Expected Result : 'w3ce'"""
sample_string= 'w3resource'
x=sample_string[0:2]
y=sample_string[-2:]
print(x+y)

"""3.	Write a Python program to replace 'cut' word to 'dog'
Sample String : 'I have a cut and I love it'
Expected Result : 'I have a dog and I love it"""
sample_string='I have a cut and I love it'
sample_string2=sample_string.replace('cut','dog')
print(sample_string2)

"""4.	Write a Python program to reverse 123  to 321 in text.
Sample String : 'I have 123 books'
Expected Result : 'I have 321 books'"""
sample_string='I have 123 books'
number="123"
reversed_number="".join(reversed(number))
print(sample_string.replace(number,reversed_number))

"""5.	Replace all occurrence of word five to one.
Sample String : "five five was a race horse, two two was one too."
Expected Result "one one was a race horse, two two was one too."""
sample_string="five five was a race horse, two two was one too."
sample_string2=sample_string.replace("five","one")
print(sample_string2)

"""6.	Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False"""
values=[1, 5, 8, 3]
print(3 in values)
print(-1 in values)

"""7.	Write a Python program to solve (x + y) * (x + y). 
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49"""
x=4
y=3
result = (x + y) ** 2
print(result)

"""8.	Write a Python program which converts float values to integer, and sum of two values, then result print with reversed order.
Test Data: x = 2,5 , y = 13.75
Expected Output: 51"""
x=2.5
y=13.75
x_int = int(x)
y_int = int(y) 
result=x_int+y_int
print(result)
reversed_result ="".join(reversed(str(result)))
print(reversed_result) 

print(my_string.find("exersice"))