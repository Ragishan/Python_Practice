#WAP to reverse a number

print("Enter the number you want to reverse" '\n')

#Using list method 
"""
n = str(input())
s = list(n)
t ='' 
for x in range(len(s)):
    t = t + s.pop()
print(t)
"""
#using while loop
n = int(input())
while n > 0:
    r = n % 10             # r = 3, 5, 1
    print(r, end="")       # 351
    n = n // 10  
    