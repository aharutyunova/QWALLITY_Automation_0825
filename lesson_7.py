# 1.Write a Python function to find the maximum value of given list (write
# algorithm).
def max_of_list(your_list):
    if (type(your_list)) != list or len(your_list) == 0:
        return "Invalid argument"

    max_item = your_list[0]
    for i in your_list:
        if max_item < i:
            max_item = i
    return max_item


print(max_of_list([10,20,3,4,2,6]))

# Anna - Correct

# 2.	Write a Python function, which will get few numbers from keyboard, return
#  to sum of them, need to write sum logic.
# Sample List : (2, 1, 4, 0, 7)
# Expected Output : 14
def sum_of_list(your_list):
    if (type(your_list)) != list or len(your_list) == 0:
        return "Invalid argument"

    sum_of_items = 0
    for i in your_list:
        sum_of_items += i

    return sum_of_items


print(sum_of_list([2, 3, 5, 6, 7]))
# Anna - Correct

# 4.	Create function, which takes 2 arguments
# •  name and surname
# •  In function create dictionary to store your name and surname
# •  Return the created dictionary

def your_info(name, surname):
    if len(name) == 0 or len(surname) == 0:
        return "invalid argument"
    info = {"name": name, "surname": surname}
    return info


print(your_info("Anna", "Hakobyan"))

# Anna - Correct

# Very Good job! I just couldn't find the solution for Task 3.
