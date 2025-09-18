def myfibonacci(n):
    a = 0
    b = 1
    list1 = []
    while a <= n:
        list1.append(a)
        a, b = b, a+b
    return list1



