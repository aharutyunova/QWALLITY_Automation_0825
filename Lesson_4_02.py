''' Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
Sample String : 'w3resource'
Expected Result : 'w3ce' '''

my_string = input("Input your string ", )
print(my_string[0:2] + my_string[-2::])

# Correct, you could also write my_string[:2] + my_string[-2:]
