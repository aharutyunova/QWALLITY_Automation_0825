# 1
first = 0
second = 1

while first<=50:
    print(first)               
    next = first + second      
    first = second             
    second = next

# 2
text="Python 3.13"
letters=sum(1 for i in text if i.isalpha())
digits=sum(1 for i in text if i.isdigit())
print(letters)
print(digits)

# 3
count=5
for i in range(count):
    print("*")
print("*"*6)

# 4

Months="July"
Month=7        
Day=31
if Months == Months or Month==7 and Day == Day:
        print("Summer")
else:
        print("Season doesn't exist")

# 5        
    
numbers=[15, 26, 28, 33]
midd=sum(numbers[len(numbers)//2 - 1 : len(numbers)//2 + 1])
median=midd/2
print(median)

numbers=[1, 4, 5, 6, 7]
midd=numbers[len(numbers)//2]
print(midd)

numbers=[[15,26,28,33],[1,4,5,6,7]]
for i in numbers:
        if len(i) % 2 == 0:
         median = (i[len(i)//2 - 1] + i[len(i)//2]) / 2
        else:
         median=i[len(i)//2]
        print(median)
            


