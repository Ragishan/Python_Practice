#Search an element in a list

lst = [11,3,5,6,7,8,9,23]
n = int(input("Enter a number to be search in the list - [11,3,5,6,7,8,9,23]") )

if n in lst:
    print(f'{n} present in the list at location {(lst.index(n))+1}')
else:
    print(f'{n} is not in this list')