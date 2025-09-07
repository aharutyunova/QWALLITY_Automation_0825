# 1
my_string = 'Here is string for your exercise!'
print(len(my_string))
# 2
str1 = "w3resource"
print(str1[0:2] + str1[-2:])
# 3
my_str = "I have a cut and I love it"
print(my_str.replace("cut", "dog"))
# 4
my_str1 = "I have 123 books"
my_str2 = my_str1.split()
my_str2[2] = ''.join(reversed(my_str2[2]))
print(' '.join(my_str2))
# 5
my_text = "five five was a race horse, two two was one too."
print(my_text.replace("five", "one"))

# 6 
my_array = [1, 5, 8, 3]
print(3 in my_array)
print(-1 in my_array)

# 7
x = 3
y = 4
z = (x + y) ** 2
a = str(z)
print("(4 + 3) ^ 2) =" + " " + a)

# 8
a = 2.5
b = 13.75
c = int(a)
d = int(b)
sum = c + d
sum1 = str(sum)
print(''.join(reversed(sum1)))