#  During program creation create your own list, tuple, dict, set.

# 1 Write a Python program to sum all the items in a list.(write logic)
# numbers_list = [10, 20, 2, 5, 6, 8]
# sum_of_numbers = 0
# for i in numbers_list:
#     sum_of_numbers += i

# print("sum of all items =", sum_of_numbers)

# 2 Write a Python program to remove duplicates from a list.
# numbers_list = [10, 20, 2, 5, 6, 8, 10, 20, 6, 5, 2]
# none_duplicates = set(numbers_list)
# print(none_duplicates)

# 3 Write a Python program which print a specified list after removing the
# 0th, 4th and 5th elements.
# numbers_list = [10, 20, 2, 5, 6, 8, 20, 3, 5, 9]
# specified_list = []

# for index, value in enumerate(numbers_list):
#     if index not in (0, 4, 5):
#         specified_list.append(value)

# print(specified_list)

# 4 Write a Python program to get the difference between the two lists.
# number_list = [10, 20, 2, 5, 6, 8, 10, 20, 6, 5, 2]
# numbers_list = [10, 20, 30, 40, 50, 6, 2, "test"]
# set1 = set(number_list)
# set2 = set(numbers_list)
# result = set1 ^ set2
# print(result)

# 5 Write a Python program to convert a tuple to a dictionary.
# students = ("Anna", "Simonyan", "37498521462", "female")
# students_dictionary = {}
# students_dictionary["name"] = students[0]
# students_dictionary["surname"] = students[1]
# students_dictionary["phone"] = students[2]
# students_dictionary["gender"] = students[3]
# print(students_dictionary)

# 6 Write a Python program to add an item in a tuple.
# students = ("Anna", "Simonyan", "37498521462", "female")
# students = students + (25,)
# print(students)

# 7 Write a Python program to add a key with corresponding value to a
# dictionary.
# Original dictionary
# my_dict = {'name': 'Ani', 'age': 25}
# my_dict['city'] = 'Yerevan'
# print(my_dict)

# 8 Write a Python program to get the maximum and minimum value in a
#  dictionary.
# my_dict = {'a': 10, 'b': 20, 'c': 5, 'd': 30}
# max_value = max(my_dict.values())
# min_value = min(my_dict.values())
# print("Maximum value:", max_value)
# print("Minimum value:", min_value)

# 9 Write a Python program to create a union of sets.
# set_1 = {1, 2, 3, 4}
# set_2 = {3, 4, 5, 6}
# union_set = set_1.union(set_2)
# print(union_set)

# 10 Write a Python program to create dict with your name, age, address,
# education, and two phone numbers.
# Create the dictionary
# info_dict = {
#     'name': 'Ani',
#     'age': 25,
#     'address': 'Yerevan, Armenia',
#     'education': 'QA Engineer',
#     'phone_numbers': ['+37412345678', '+37498765432']
# }
# print(info_dict)
