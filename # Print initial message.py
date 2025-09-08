# Print initial message
print("It's my first program", end="!\n")

# Personal information
name = "Hamlet"
surname = "Balasanyan"
print(name + " " + surname, "\n")

# Backround information
print("I'm Hamlet Balasanyan, from Goris." "\n"
      "I work as a QA engineer at Digitain Armenia." "\n"
      "Apart from my job, I enjoy watching and playing football." "\n"
      "My favorite football club is Liverpool")

# Simple arithmetic operation
a, b = 11, 15
sum = a + b
print(sum)

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



