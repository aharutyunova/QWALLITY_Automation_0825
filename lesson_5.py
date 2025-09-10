#  During program creation create your own list, tuple, dict, set.

# 1 Write a Python program to sum all the items in a list.(write logic)
my_list = 1, 3, 4, 50, 35
sum_of_list_items = 0
for item in my_list:
    sum_of_list_items += item
print(sum_of_list_items)

# 2 Write a Python program to remove duplicates from a list.
first_list = "dog", 1, False, 2, 2, "dog", "cat"
final_list = list(set(first_list))
print(final_list)

# 3 Write a Python program which print a specified list after removing the 0th, 4th and 5th elements.
given_list = [1, 4, 23, "test", "go", 45, "all"]
del given_list[5]
del given_list[4]
del given_list[0]
print(given_list)

# 4 Write a Python program to get the difference between the two lists.
list_1 = 10, 20, 30, "to", "star", 45
list_2 = 20, 34, 12, "all", "to", 0

diff_1 = set(list_1) - set(list_2)
diff_2 = set(list_2) - set(list_1)
diff = list(diff_1) + list(diff_2)
print(diff)

# 5 Write a Python program to convert a tuple to a dictionary.
my_tuple = (("name", "Anna"), ("surname", "Bznuni"), ("age", 28))
my_dict = dict(my_tuple)
print(my_dict)

# 6 Write a Python program to add an item in a tuple.
my_tuple = (44, 55, "hello", "done")
new_tuple = my_tuple + (23,)
print(new_tuple)

# 7 Write a Python program to add a key with corresponding value to a dictionary.
my_dict = {"name": "Anna", "surname": "Bznuni"}
my_dict["age"] = 28
print(my_dict)

# 8 Write a Python program to get the maximum and minimum value in a dictionary.
my_dict = {"a": 25, "b": 78, "c": 12, "d": 90, "e": 45}
max_value = max(my_dict.values())
min_value = min(my_dict.values())
print("Maximum value:", max_value)
print("Minimum value:", min_value)

# 9 Write a Python program to create a union of sets.
set_1 = {1, 3, 5, 22, 44, 55}
set_2 = {1, 3, 66, 77, 22, 99}
union_of_sets = set_1.union(set_2)
print(union_of_sets)

# 10 Write a Python program to create dict with your name, age, address, education, and two phone numbers.
my_own_dict = {
    "name": "Anna",
    "surname": "Bznuni",
    "age": 28,
    "address": "Yerevan",
    "phone_number": +37477777778,
    "additional_phone_number": +10099283984
}
