#Write a Python program to get the Fibonacci series between 0 to 50. /
# Note : The Fibonacci Sequence is the series of numbers : /
# 0, 1, 1, 2, 3, 5, 8, 13, 21, .... Every next number is found by adding up the two numbers before it./
# Expected Output : 0 1 1 2 3 5 8 13 21 34

numbers = []
n = 50
a = 0
b = 1
c = 0

while a <= n:
    numbers.append(a)

    c = a + b
    a = b
    b = c

print(numbers)

# Anna - Correct

#Write a Python program that accepts a string and calculate the number of digits and letters.   
# Sample Data: Python 3.13
# Expected Output:
# Letters 6
# Digits 3

data1="python"
data2="3.13"
data = data1 + data2
print(data)

digits=0
letters=0

for ch in data: 
    if ch.isalpha():  
        letters = letters + 1
    elif ch.isdigit():    
        digits = digits + 1
          
print(letters)
print(digits)

# Anna - Correct

#Write a Python program to print alphabet pattern 'L'  
# Expected Output:
# *                                                                      
# *                                                                      
# *                                                                      
# *                                                                      
# *                                                                      
# *                                                                      
# *****

rows = 7
cols = 5

for i in range(rows):
    if i < rows - 1:
        print("*")              
    else:
        print("*" * cols)     
 # Anna - Correct


#Write a Python program that reads two integers representing a month and day and prints the season for that month and day.  
# Expected Output:
# Month: July(7)                   
# Day: 31   
# Season: Summer                                                    
# month=7
# day=31

season={12:"winter", 1:"winter", 2:"winter",3:"spring",4:"spring",5:"spring",
        6:"summer",7:"summer",8:"summer",9:"autumn",10:"autumn",11:"autumn"}
months=["January","February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]
month=int (input("enter month"))
day=int(input("enter day"))

season_result=season[month]

print(month)
print(day)
print(season_result)

# TODO The general solution is correct, but you didn't handle incorrect month/day cases

#Write a Python program to find the median of few values. 
# Expected Output:
# numbers: 15, 26, 28, 33   or   1, 4, 5, 6, 7
                                                 
numbers=[15,26,28,33]
n=len(numbers)
if n % 2:
    median = numbers[n // 2]
else:
 median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
print (median)

#or 
numbers2 = [1, 4, 5, 6, 7]
n2 = len(numbers2)

if n2 % 2 == 1:
    median2 = numbers2[n2 // 2]
else:    
    median2 = (numbers2[n2 // 2 - 1] + numbers2[n2 // 2]) / 2
print(median2)

# Anna - Correct