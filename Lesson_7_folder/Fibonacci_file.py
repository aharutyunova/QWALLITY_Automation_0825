def fib(x):
    fib_list = [0, 1]
    y = 1
    for i in fib_list:
        y += i
        if y >= x:
            break 
        fib_list.append(y)
    return (fib_list)


print(fib(70))
