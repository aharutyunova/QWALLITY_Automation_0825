'''1.	Write a Python program to get the Fibonacci series between 0 to 50. 
Note : The Fibonacci Sequence is the series of numbers : 
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 0 1 1 2 3 5 8 13 21 34
'''
a = 0
b = 1
list1 = []
while a <= 50:
    list1.append(a)
    a, b = b, a+b
print(list1)    

# Anna - Correct

'''2.	Write a Python program that accepts a string and calculate the number of digits and letters.  
Sample Data: Python 3.13
Expected Output:
Letters 6
Digits 3
'''
text1 = "Python 3.13"
letters = 0
digits = 0
for i in text1:
    if '0' <= i <= '9':
        digits += 1
    elif 'a' <= i <= 'z' or 'A' <= i <= 'Z':
        letters += 1
               

print(digits) 
print(letters)

# Anna - Correct

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
for i in range(6):
    print("*")
print("*****")    

# Anna - Correct
'''
4.	Write a Python program that reads two integers representing a month and day and prints the season for that month and day.  
Expected Output:
Month: July(7)                   
Day: 31   
Season: Summer                                                    

'''
# day = int(input("Enter day: "))


# if 1 <= day <= 31:
#     month = int(input("Enter month: "))
#     if month in range(3, 6):
#         print("Spring")
#     elif month in range(6, 9):
#         print("Summer")
#     elif month in range(9, 12):
#         print("Autumn")
#     elif month in range(1, 3) or month == 12:
#         print("Winter")
#     else:
#         print("Entered month is not correct")    
# else:
#     print("Entered day is not correct")     

# Anna – generally correct. Please also check the sample solution.

'''
5.	Write a Python program to find the median of few values. 
Expected Output:
numbers: 15, 26, 28, 33   or   1, 4, 5, 6, 7
                                                 
'''
list5 = [15, 26, 28, 33, 10]
list5.sort()
len5 = len(list5)
if len5 % 2 == 1:
    median = list5[len5//2]
else:
    median = (list5[len5//2 - 1] + list5[len5//2])/2
print(median)        

# Anna - Correct