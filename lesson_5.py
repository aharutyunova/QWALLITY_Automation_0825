# 1.Write a Python program to sum all the items in a list.(write logic)
mylist = [5, 14, 45, 61, 11, 22, 7]
sum_of_list = 0
for i in mylist:
    sum_of_list += i

print(sum_of_list)


# 2.Write a Python program to remove duplicates from a list.
this_list = [5, 14, 5, 11, 11, 22, 7, 88, "apple", "orange", "lemon", "apple"]

unique_list = []
for x in this_list:
    if x not in unique_list:
        unique_list.append(x)

print(unique_list)

# 3.Write a Python program which print a specified list after removing the 0th,
# 4th and 5th elements.
specified_list = [5, 14, 5, 11, 11, 22, 7, 88, "apple", "orange"]
removeing_indexes = [0, 4, 5]

for item in sorted(removeing_indexes, reverse=True):
    specified_list.pop(item)

print(specified_list)

# 4.Write a Python program to get the difference between the two lists.
list_one = [5, 14, 5, 11, 11, 22, 7, 88, "apple", "orange"]
list_two = [7, 14, 45, 61, 11, 22, 7]

difference = []

for i in list_one:
    if i not in list_two and i not in difference:
        difference.append(i)


for i in list_two:
    if i not in list_one and i not in difference:
        difference.append(i)

print(difference)

# 5.Write a Python program to convert a tuple to a dictionary.
my_tuple = (("a", 1), ("b", 2), ("c", 3))

my_dict = dict(my_tuple)

print(my_dict)

# 6.Write a Python program to add an item in a tuple.
my_tuple1 = ("apple", "banana", "orange")
tuple_to_list = list(my_tuple1)

tuple_to_list.append("car")
my_tuple1 = tuple(tuple_to_list)

print(my_tuple1)

# 7.Write a Python program to add a key with corresponding value
#  to a dictionary.
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict["driver"] = "Hamlet"

print(thisdict)
# 8.Write a Python program to get the maximum and minimum value in a
#  dictionary.
numbersdict = {
    "number1": 15,
    "number2": 26,
    "number3": 1,
    "number4": -5
}

max_value = max(numbersdict.values())
min_value = min(numbersdict.values())

print("Maximim Value = ", max_value, "Minimum value = ", min_value)

# 9.Write a Python program to create a union of sets.
first_set = {"Banana", "apple", "orange"}
second_set = {1, 2, 3}

union_set = first_set | second_set

print(union_set)

# 10.Write a Python program to create dict with your name, age, address,
# education, and two phone numbers.
person_info = {
    "name": "Hamlet Balasanyan",
    "age": 25,
    "address": "Yerevan, Armenia",
    "education": "Bachelor's in Management",
    "phone_numbers": ["+374 91 123456", "+374 94 654321"]
}

print(person_info)
