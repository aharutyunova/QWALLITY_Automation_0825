#  During program creation create your own list, tuple, dict, set.
# #1 Write a Python program to sum all the items in a list.(write logic)

my_own_list = ['breakfast', 'lunch', 'dinner', 'breakfast', 2025, '09 September']
print(my_own_list)

my_own_tuple = ('breakfast', 'lunch', 'dinner', 'breakfast',  2025, '09 September')
print(my_own_tuple)

my_own_set = {'breakfast', 'lunch', 'dinner', 'breakfast',  2025, '09 September'}
print(my_own_set)

my_own_dict = {"breakfast" : "eggs", "lunch": "soup", "dinner": "salad", "year": 2025, "month": "September" }
print(my_own_dict)

list_to_sum = [1,2,3,4,5,6]
sum = 0
for n in list_to_sum:
    sum = sum + n

print(sum)
