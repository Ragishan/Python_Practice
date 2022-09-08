#WAP to enter a number from user between 1 to 5 and print its character format.
import inflect
p = inflect.engine()

print('Please enter 5 numbers','\n')
n = [p.number_to_words(int(input())) for x in range(5)]
print(f'You entered {n}')