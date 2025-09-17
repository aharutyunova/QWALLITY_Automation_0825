#  During program creation create your own list, tuple, dict, set.

#1 Write a Python program to sum all the items in a list.(write logic)
list_1 = [10, 20, 40]
sum = 0
for i in list_1:
    sum += i
print(sum)


#2 Write a Python program to remove duplicates from a list.
list_2 = [10, 20, 10, 20, 30]
newlist_2 = set(list_2)
print(newlist_2)

#3 Write a Python program which print a specified list after removing the 0th, 4th and 5th elements. 
list_3 = [0, 1, 2, 3, 4, 5, 6] 
del list_3[4:6]
del list_3[0]
print(list_3)

#4 Write a Python program to get the difference between the two lists.
l1 = [1, 2, 3, 45]
l2 = [2, 45, 6]
l12 = set(l1).difference(set(l2))
l21 = set(l2).difference(set(l1))
print(l12.union(l21))

#5 Write a Python program to convert a tuple to a dictionary.
tuple_1 = ('apple', 'banana', 'cherry')
dict_1 = {}
index = 0 
for i in tuple_1:
    dict_1[index] = i
    index += 1

print(dict_1)


#6 Write a Python program to add an item in a tuple.
tuple_2 = (1, 2, 5)
list_6 = list(tuple_2)
list_6.append(8)
newtup = tuple(list_6)
print(newtup)

#7 Write a Python program to add a key with corresponding value to a dictionary.


#8 Write a Python program to get the maximum and minimum value in a dictionary.

#9 Write a Python program to create a union of sets.

#10 Write a Python program to create dict with your name, age, address, education, and two phone numbers. 
