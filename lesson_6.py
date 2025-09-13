# task N 1
fib_nums = [0, 1]
while fib_nums[-1] + fib_nums[-2] <= 50:
    fib_nums.append(fib_nums[-1] + fib_nums[-2])
print(fib_nums)


# task N 2
user_input = input("Please type: ")
digits = 0   # calc int
letters = 0  # calc string
for i in user_input:
    if '0' <= i <= '9':
        digits += 1
    elif ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
        letters += 1
print("Digits:", digits)
print("Letters:", letters)


# task N 3
for i in range(6):
    print('*', end='\n')
for j in range(5):
    print("*", end=" ")


# task N 4
days_in_month = {
    1: 31, 2: 28, 3: 31,
    4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30,
    10: 31, 11: 30, 12: 31
}

month_names = {
    1: "January", 2: "February", 3: "March",
    4: "April", 5: "May", 6: "June",
    7: "July", 8: "August", 9: "September",
    10: "October", 11: "November", 12: "December"
}


user_input_month = int(input("Please type Month (1-12): "))
user_input_day = int(input("Please type Day: "))

if user_input_month in days_in_month:
    max_day = days_in_month.get(user_input_month)
    if 1 <= user_input_day <= max_day:

        if user_input_month in [12, 1, 2]:
            season = "Winter"
        elif user_input_month in [3, 4, 5]:
            season = "Spring"
        elif user_input_month in [6, 7, 8]:
            season = "Summer"
        elif user_input_month in [9, 10, 11]:
            season = "Autumn"
        print(f"Season: {season}")
    else:
        print("Invalid day for that month.")
else:
    print("Invalid month.")


# task N 5
input_numbers = input("Please input your number: ")
length = len(input_numbers)

if length % 2 == 0:
    mid1 = int(input_numbers[length // 2 - 1])
    mid2 = int(input_numbers[length // 2])
    result = (mid1 + mid2) / 2
    print(f'Result even numbers: {result}')
else:
    mid = int(input_numbers[length // 2])
    print("Result (odd length):", mid)
