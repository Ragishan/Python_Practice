# WAP to find the highest and lowest age among 5 people

n = [int(input()) for x in range(5)]
n.sort()
print(f'Highest age is {n[4]}')
print(f'Lowest age is {n[0]}' )