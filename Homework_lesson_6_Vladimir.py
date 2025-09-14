# 1
my_list = [0, 1]
c = 1
for i in my_list:
    c += i
    my_list.append(c)
    if c > 50:
        my_list.pop()
        print(my_list)
        break

# Anna - Correct

# 2
s = "Python 3.13"
digit = 0
letter = 0
for i in s:
    if i.isalpha():
        letter += 1
    elif i.isdigit():
        digit += 1
print("Letter =", letter)
print("digit =", digit)

# Anna - Correct

# 3
for a in range(11):
    if a < 6:
        print("*")
    else:
        print("*", end=" ")
print()

# Anna - Correct
# 5 
numbers = [1, 2, 3, 4, 7, 8, 9, 10]
a = 0
b = 0
if len(numbers) % 2 == 0:
    a = len(numbers) // 2
    print("Median :", numbers[a-1], numbers[a])
else:
    b = (len(numbers) - 1) // 2
    print("median", numbers[b])
# TODO: In your example, the median should be calculated as (numbers[a-1] + numbers[a])/2 
# because when the list has an even number of elements, the median is the average of the two middle numbers.

# 4
mounth_info = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 
               6: "June", 7: "July", 8: "August", 9: "September", 
               10: "October", 11: "November", 12: "December"}
days_in_month = {
    1: 31, 2: 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31
}
season = ["Spring", "Summer", "Autumn", "Winter"]
mounth = int(input("Input Mounth"))

if mounth in mounth_info.keys():
    day = int(input("Input Day"))
    if 1 <= day <= days_in_month[mounth]:
        if mounth in [12, 1, 2]:
            my_season = season[3]
        elif mounth in [3, 4, 5]:
            my_season = season[0]
        elif mounth in [6, 7, 8]:
            my_season = season[1]
        elif mounth in [9, 10, 11]:
            my_season = season[2]
    print(f"{day} {mounth_info[mounth]} {days_in_month[mounth]} {my_season}")
else:
    print("Invalid day or mounth")

# TODO: You should define the `my_season` variable outside of the if-block to make it visible outside of the conditional block.
# Also, you didn’t handle the case of an invalid day (e.g., day not in the valid range for the given month).
