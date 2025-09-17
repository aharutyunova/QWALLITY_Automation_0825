"""
1.  Write a Python function to find the maximum value of given list (write algorithm)."""
list=[10, 22,35,78,345,18]
def max_value(list):
    max=list[0]
    for i in list:
        if i>max:
            max=i
    return max
print (max_value(list))
"""2.   Write a Python function, which will get few numbers from keyboard, return to sum of them, need to write sum logic.
Sample List : (2, 1, 4, 0, 7)
Expected Output : 14"""
def sum_numbers(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum
print (sum_numbers(2,0,1,90,3))
"""3.   Create module where keep function of Fibonacci, in second .py file import and call it."""
def fibonacci(n):
    """Return Fibonacci sequence up to n terms"""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
"""4.   Create function, which takes 2 arguments
•  name and surname
•  In function create dictionary to store your name and surname
•  Return the created dictionary"""
def create_dict(name,surname):
    my_dict={"name":name,"surname":surname}
    return my_dict
print(create_dict("Anna","Grigoryan"))