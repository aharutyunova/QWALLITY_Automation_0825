"""
1.	Write a Python function to find the maximum value of given list (write algorithm).
"""

our_given_list = [1, 5, 43, 4, 73]


def get_max_value(given_list):
    max_value = given_list[0]
    for i in given_list:
        if i > max_value:
            max_value = i
        else:
            continue
    return max_value


print(get_max_value(our_given_list))

# TODO: range() excludes the last value, so don't subtract 1 — just use:
# for i in range(len(given_list)):

"""
2.	Write a Python function, which will get few numbers from keyboard, return to sum of them, need to write sum logic.
Sample List : (2, 1, 4, 0, 7)
Expected Output : 14
"""


def sum_of_numbers(numbers):
    sum_item = 0
    for n in numbers:
        sum_item += n
    return sum_item


inputted_numbers = input("Enter numbers separated by spaces: ")

list_1 = []

for x in inputted_numbers.split():
    if x.isdigit():
        list_1.append(int(x))
    else:
        print("Please enter only numbers.")
        break
else:
    print("Sum:", sum_of_numbers(list_1))

# Anna - Good solution
"""
3.	Create module where keep function of Fibonacci, in second .py file import and call it.
"""

from pre_lesson_7 import Fibonacci_file

print(Fibonacci_file.fibonacci(0, 1, 50))
# Anna - Correct
"""
4.	Create function, which takes 2 arguments
•  name and surname
•  In function create dictionary to store your name and surname
•  Return the created dictionary
"""


def name_and_surname(name, surname):
    n_and_sname = {"name": name, "surname": surname}
    return n_and_sname


print(name_and_surname("Anna", "Bznuni"))

# Anna - Correct

# Good job! Please pay attention to my TODO in Task 1.
