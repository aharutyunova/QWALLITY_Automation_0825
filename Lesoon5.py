# 1 Write a Python program to sum all the items in a list.(write logic)
numbers = [1, 2, 3, 4, 5, 6]
total = sum(numbers)
print(total)

# TODO: I expected an implementation of the sum algorithm, not the use of the built-in sum() function.

# 2 Write a Python program to remove duplicates from a list.
numbers = [1, 2, 3, 4, 5, 6, 5, 2, 1]
filtered = list(set(numbers))
print(filtered)

# Anna - Correct

# 3 Write a Python program which print a specified list after removing the 0th, 4th and 5th elements.  
numbers = [1, 2, 3, 4, 5, 6]
numbers.remove(numbers[0])
numbers.remove(numbers[4])
print(numbers)


# I have a question related to the 5th element. When we removing the 0th element the total element count become less than 5. So I get error when doing numbers.remove(numbers[5])
# TODO Use a list with more than 5 elements, or handle the error if the list is too short. 
# Remember: when you remove items by index, the list changes and indexes shift. 
# To avoid mistakes, remove items starting from the end.
# numbers.remove(numbers[5])
# numbers.remove(numbers[4])
# numbers.remove(numbers[0])

# 4 Write a Python program to get the difference between the two lists.
numbers = [1, 2, 3, 4, 5, 6]
numbers2 = [1, 2, 113, 234, 5, 6]
difference = set(numbers) ^ set(numbers2)
print(difference)

# TODO: This solution is generally correct,
# but once we cover loops and conditions, it would be better 
# to check whether each element exists in one list and is absent in the other, 
# since sets automatically remove duplicates.

# 5 Write a Python program to convert a tuple to a dictionary.
colors = ["red", "blue", "green", "yellow"]
newcolors = dict(enumerate(colors))
print(newcolors)

# Anna - Good approach

# 6 Write a Python program to add an item in a tuple.
colors = ["red", "blue", "green", "yellow"]
colors.append("black")
print(colors)

# TODO: You added an item to the list, not to a tuple.

# 7 Write a Python program to add a key with corresponding value to a dictionary.
colors = {0: 'red', 1: 'blue', 2: 'green', 3: 'yellow'}
colors[4] = 'purple'
print(colors)
# Anna - Correct

# 8 Write a Python program to get the maximum and minimum value in a dictionary.
colors = {0: 125, 1: 523, 2: 224, 3: 362}
print(colors[min(colors)], colors[max(colors)])

# TODO: In your solution, you compared the max and min keys, not the values. 
# You should get the values first and then find the max/min.
print(max(list(colors.values())))
print(min(list(colors.values())))


# 9 Write a Python program to create a union of sets.
numbers = {1, 2, 3, 4, 5, 6}
numbers2 = {1, 2, 113, 234, 5, 6}
diff = numbers.union(numbers2)
print(diff)

# Anna - Correct

# 10 Write a Python program to create dict with your name, age, address, education, and two phone numbers. 
my_info = {}
my_info = {
    'Name': "Ruzanna",
    "Age": 25,
    "Address": "Yerevan",
    "Education": "bachelor",
    "Phone number": 5555222225,
    "Phone number1": 5555552220

}
print(my_info)
# TODO: It would be better to keep phone numbers as a list
my_info = {
    'Name': "Ruzanna",
    "Age": 25,
    "Address": "Yerevan",
    "Education": "bachelor",
    "Phone number": [5555222225, 5555552220]
}