# 3
from Lesson_7_folder import Fibonacci_file

Fibonacci_file.fib(80)


# 1
def get_max_value(my_list):
    max_value = 0
    for i in my_list:
        if i > max_value:
            max_value = i
    return max_value


print(get_max_value([1, 8, -8, 78]))

# 2


def get_sum_of_numbers():
    numbers = input("Enter a few number with probels ").split(" ")
    sum_numbers = 0
    for a in numbers:
        sum_numbers += int(a)
    return sum_numbers


print(get_sum_of_numbers())

# 4


def full_name(name, surname):
    my_full_name = {"my_name": name, "my_surname":  surname}
    return my_full_name


print(full_name("Vladimir", "Voskanyan"))
