# 3.	Create module where keep function of Fibonacci, in second .py file import
# and call it.

def fibonacci():
    numbers = [0, 1]
    while True:
        next_number = numbers[-1] + numbers[-2]
        if next_number > 50:
            break
        numbers.append(next_number)

    return "Fibonacci series up to 50:", numbers

