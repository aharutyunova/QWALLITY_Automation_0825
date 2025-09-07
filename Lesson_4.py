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

#1.	Write a Python program to calculate the length of a string.
my_string = 'Here is string for your exercise!'
x = len(my_string)
print(x)
# Anna - Correct

#2.	Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
string_1 = 'w3resource'
print(string_1[0],string_1[1],string_1[8],string_1[9])
# TODO - would be better to use indexes for solution 
result = string_1[:2] + string_1[-2:]
print(result)



#3.Write a Python program to replace 'cut' word to 'dog'
string2 = 'I have a cut and I love it'
new = string2.replace('cut','dog')
print(new)
# Anna - Correct

#4.Write a Python program to reverse 123  to 321 in text.

string3 = 'I have 123 books'
new = string3.split()
a = new[2]
b = ''.join(reversed(a))
print(f"I have {b} books")
# Anna - Correct

#5.Replace all occurrence of word five to one.
string4 = "five five was a race horse, two two was one too."
new_text = string4.replace('five', 'one')
print(new_text)
# Anna - Correct

#6.Write a Python program to check whether a specified value is contained in a group of values.
test_data =[1, 5, 8, 3]
print(3 in test_data)
print(9 in test_data)
# Anna - Correct

#7.	Write a Python program to solve (x + y) * (x + y). 
z = 4
c = 3
result = (z + c) ** 2

print(result)
# Anna - Correct

#8.	Write a Python program which converts float values to integer, and sum of two values, then result print with reversed order.
p = 2.5
o = 13.75
sum = int(p) + int(o)
string8 = str(sum)
print(''.join(reversed(string8)))
# Anna - Correct

# Good Job, Please pay attention on my #TODO comment for task 2
