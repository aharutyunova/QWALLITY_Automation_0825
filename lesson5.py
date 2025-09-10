#  During program creation create your own list, tuple, dict, set.

values=[1,2,3,4,5,6,7,8,9,9]

#1 Write a Python program to sum all the items in a list.(write logic)
print("The sum is list:", sum(values))

#2 Write a Python program to remove duplicates from a list.
uniques = list(set(values))
print("unique list is:", uniques)  

#3 Write a Python program which print a specified list after removing the 0th, 4th and 5th elements.  
values.pop(0)
values.pop(4)
values.pop(5)
print("removed 0th, 4th,5th elements:", values)

#4 Write a Python program to get the difference between the two lists.

values2=[1,2,2,2,3,4,5,6,7,0,8,9]
diff1 = [x for x in values if x not in values2]
diff2 = [x for x in values2 if x not in values]

diff_all = diff1 + diff2
print("In values but not in values2:", diff1)
print("In values2 but not in values:", diff2)
print("Difference between lists:", diff_all)

#5 Write a Python program to convert a tuple to a dictionary.

tuple_data = (("a", 1), ("b", 2), ("c", 3))
result = dict(tuple_data)
print("Converted dictionary:", result)

#6 Write a Python program to add an item in a tuple.

tuple = (1, 2, 3)
new_tuple = tuple + (4,)
print(new_tuple)


#7 Write a Python program to add a key with corresponding value to a dictionary.
dict = {"a": 1, "b": 2}
dict["c"] = 3
print("Updated dictionary:", dict)

#8 Write a Python program to get the maximum and minimum value in a dictionary.

min_value = min(dict.values())
max_value = max(dict.values())
print("Min in dictionary:", min_value)
print("Max in dictionary:", max_value)

#9 Write a Python program to create a union of sets.

set1 = {1,2,3}
set2 = {4,5,6}
unioned = set1.union(set2)
print("union set is:", unioned)

#10 Write a Python program to create dict with your name, age, address, education, and two phone numbers. 
dictMyInfo = {"name": "Anna", "age": 27, "address":"home", "education": "higher" , "phones": [12345,12345]}