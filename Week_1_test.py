# 1. Reverse a string using a for loop in Python.

string = input()
for i in range(len(string) - 1, -1, -1):
    print(string[i], end='')


# 2. Write a Python program to find the sum of all numbers in a list using a for loop.

l = [2, 5, 6, 12]
for i in range(len(l)):
    sum += l[i]
print(f'sum of all numbers in a list: {sum}')


# 3. Write a Python program that checks whether a given number is even or odd using an if-else statement.

n = int(input('Enter the number '))
if n%2==0:
    print('The number is even')
else:
    print('The number is odd')


# 4. Implement a program to determine if a year is a leap year or not using if-elif-else statements.

year = int(input())
if len(str(year))==4:
    if year%4==0:
        print('The year is leap year')
    else:
        print('The year is not a leap year')


# 5. Use a lambda function to square each element in a list

l = [1,2,3,4]
square = list(map(lambda n: n**2, l))
print(square)


# 6. Write a lambda function to calculate the product of two

product = lambda a,b : a*b
print(product(2,5))

