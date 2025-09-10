#  During program creation create your own list, tuple, dict, set.

# 1 Write a Python program to sum all the items in a list.(write logic)
my_list = [1, 86, 75, 25, 258, 6977, 158]
total = 0
for num in my_list:
    total += num
print(total)

# 2 Write a Python program to remove duplicates from a list.
my_list = ['1', '3', '5', '3', '9']
check_double = list(set(my_list))
print(check_double)

# 3 Write a Python program which print a specified list after removing the 0th,
# 4th and 5th elements.
my_list3 = ['test', 'car', 'apple', 'var', 'python', 'sport']
my_list3.remove(my_list3[0])
my_list3.remove(my_list3[-1])
my_list3.remove(my_list3[-1])
print(my_list3)

# 4 Write a Python program to get the difference between the two lists.
x = ['test', 'car', 'apple', 'var', 'python', 'sport', 'dog']
y = ['car', 'test', 'var', 'apple', 'sport', 'python', 'cat']
x_set = set(x)
y_set = set(y)
print(x_set.difference(y_set), y_set.difference(x_set))

# 5 Write a Python program to convert a tuple to a dictionary.
my_tuple = (('car', 'apple'), ('python', 'sport'))
tuple_to_list = dict(my_tuple)
print(tuple_to_list)

# 6 Write a Python program to add an item in a tuple.
x = ('Name', 'Surname')
x = x + ('Fullname', 'Birthday')
print(x)

# 7 Write a Python program to add a key with corresponding value
# to a dictionary.
car = {
    "Mark": "Mercedes",
    "Model": "E class"
        }
car["Realsed_year"] = "2025"
print(car)

# 8 Write a Python program to get the maximum and minimum value
# in a dictionary.

warehouse = {
    "Book": 26,
    "pen": 98,
    "Ruler": 4,
    "pencil": 206
    }
x = warehouse.values()
print("Max value:", max(x))
print("Min value:", min(x))

# 9 Write a Python program to create a union of sets.
x = {'orange', 'banana', 'water', 'boy'}
y = {'car', 'book', 'water', 'orange'}
print(x.union(y))

# 10 Write a Python program to create dict with your name, age, address,
# education, and two phone numbers.
my_info = {
    "LastName": "Ruben",
    "FirstName": "Asatryan",
    "Age": "29",
    "FullName": "Ruben Asatryan",
    "Phone number": "+374006566",
    "email": "example2025@gmail.com"
    }
print(my_info)
