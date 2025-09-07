1.
my_string = 'Here is string for your exercise!'
x=len(my_string)
print(x)

2.
x='w3resource'
print(x[0:2]+x[-2:])

3. 
x='I have a cat and I love it'
y=x.replace('cat',"dog")
print(y)

4. 
digits=''.join(reversed('123'))
x=f'I have {digits} books'
print(x)


5.
x= "five five was a race horse, two two was one too"
y=x.replace("five","two")
print(y)

6.
x=[1, 5, 8, 3]
y=[1, 5, 8, 3]
print(3 in x)
print(-1 in y)

7.
x=4
y=3
z=(x+y)*(x+y)
result=f"(4+3)^2={z}"
print(result)

8.
x = 2.5
y = 13.75
z = int(x)+int(y)
print(int("".join(reversed(str(z)))))
