n = int(input("Enter limit "))

a = 0
b = 1

for i in range(0,n):
    print(a, end="  ")
    c = a + b
    a = b
    b = c