"""
1.	Write a Python function to find the maximum value of given list (write algorithm)."""

def maxvalue(l):
    maxvalue = l[0]
    for i in l:
        if i > maxvalue:
            maxvalue = i
    return maxvalue

l1 = [8, 7, 4, 11]
print(maxvalue(l1))

"""2.	Write a Python function, which will get few numbers from keyboard, return to sum of them, need to write sum logic.
Sample List : (2, 1, 4, 0, 7)
Expected Output : 14"""
def sum_num():
    numbers = input("Enter numbers")
    l =[]
    for i in numbers:
        l.append(int(i))
    totalsum = 0
    for j in l:
        totalsum += j
    return totalsum
x = sum_num()
print(x)

def sum_num2(*args):
    res = sum(args)
    return res

print(sum_num2(5, 4))

"""3.	Create module where keep function of Fibonacci, in second .py file import and call it."""
from Myfunction import Fibonacci

print(Fibonacci.myfibonacci(50))

"""4.	Create function, which takes 2 arguments 
•  name and surname
•  In function create dictionary to store your name and surname
•  Return the created dictionary

"""
def myData(myname, mysurname):
    my_dict = {"name": myname, "surname": mysurname}
    return my_dict

print (myData("Anush", "Khachaturyan"))