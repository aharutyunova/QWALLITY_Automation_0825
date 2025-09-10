# 1 Write a Python program to sum all the items in a list.(write logic)
numbers = [1, 2, 3, 4, 5, 6]
total = sum(numbers)
print(total)

# 2 Write a Python program to remove duplicates from a list.
numbers = [1, 2, 3, 4, 5, 6, 5, 2, 1]
filtered = list(set(numbers))
print(filtered)


# 3 Write a Python program which print a specified list after removing the 0th, 4th and 5th elements.  
numbers = [1, 2, 3, 4, 5, 6]
numbers.remove(numbers[0])
numbers.remove(numbers[4])
print(numbers)

# I have a question related to the 5th element. When we removing the 0th element the total element count become less than 5. So I get error when doing numbers.remove(numbers[5])


# 4 Write a Python program to get the difference between the two lists.
numbers = [1, 2, 3, 4, 5, 6]
numbers2 = [1, 2, 113, 234, 5, 6]
difference = set(numbers) ^ set(numbers2)
print(difference)

# 5 Write a Python program to convert a tuple to a dictionary.
colors = ["red", "blue", "green", "yellow"]
newcolors = dict(enumerate(colors))
print(newcolors)

# 6 Write a Python program to add an item in a tuple.
colors = ["red", "blue", "green", "yellow"]
colors.append("black")
print(colors)

# 7 Write a Python program to add a key with corresponding value to a dictionary.
colors = {0: 'red', 1: 'blue', 2: 'green', 3: 'yellow'}
colors[4] = 'purple'
print(colors)

# 8 Write a Python program to get the maximum and minimum value in a dictionary.
colors = {0: 125, 1: 523, 2: 224, 3: 362}
print(colors[min(colors)], colors[max(colors)])

# 9 Write a Python program to create a union of sets.
numbers = {1, 2, 3, 4, 5, 6}
numbers2 = {1, 2, 113, 234, 5, 6}
diff = numbers.union(numbers2)
print(diff)

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
