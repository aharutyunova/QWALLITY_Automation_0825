# 3
from Lesson_7_folder import Fibonacci_file

Fibonacci_file.fib(80)

# Anna - Correct

# 1
def get_max_value(my_list):
    max_value = 0
    for i in my_list:
        if i > max_value:
            max_value = i
    return max_value


print(get_max_value([1, 8, -8, 78]))

# TODO: The logic is mostly correct, but it's better to set max_value to the first element of the list.
#       This way, the function works even if all numbers are negative.


# 2


def get_sum_of_numbers():
    numbers = input("Enter a few number with probels ").split(" ")
    sum_numbers = 0
    for a in numbers:
        sum_numbers += int(a)
    return sum_numbers


print(get_sum_of_numbers())

# Anna - Correct

# 4

def full_name(name, surname):
    my_full_name = {"my_name": name, "my_surname":  surname}
    return my_full_name


print(full_name("Vladimir", "Voskanyan"))
# Anna - Correct

# Good Job!!!