# Task N3
from Fib import lesson_Test

# 1. Write a Python function to find the maximum value of
# given list (write algorithm).


def find_max_value():

    numbers_input = input("Please type number with space(exc. 10, 5, 33): ")

    str_numbers = numbers_input.split(',')

    numbers = []
    for n in str_numbers:
        numbers.append(int(n))

    max_value = numbers[0]

    for num in numbers[1:]:
        if num > max_value:
            max_value = num

    print("Max value is", max_value)


find_max_value()

# 2. Write a Python function, which will get few numbers from keyboard,
# return to sum of them, need to write sum logic.
# Sample List : (2, 1, 4, 0, 7)
# Expected Output : 14


def sum_value():
    numbers = input("Please type number with space: ")
    num_list = numbers.split()
    total = 0
    for num in num_list:
        total += int(num)

    print("Expected Output:", total)


sum_value()

# 3. Create module where keep function of Fibonacci, in second .py file import
# and call it.

lesson_Test.fib_num()


# 4. Create function, which takes 2 arguments
# • name and surname
# • In function create dictionary to store your name and surname
# • Return the created dictionary

def my_data(firstName, lastName):
    my_dict = {
        "firstName": firstName,
        "lastName": lastName
    }
    return my_dict


my_name = (input("Type your name: "))
my_surname = (input("Type your surname: "))

result = my_data(my_name, my_surname)
print("Expected result: ", result)
