#program to help understand the concept of recursion in python
#Recursion is a method of solving problems that involves breaking a problem down into smaller and smaller subproblems until you get to a small enough problem that it can be solved trivially.

def factorial(n):
    if n == 0:
        return 1

    else:
        return n * factorial(n - 1)
    
num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}") #print the factorial of the number entered by the user

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
num2 = int(input("Enter a number: "))
print(f"The fibonacci of {num2} is {fibonacci(num2)}") #print the fibonacci of the number entered by the user

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def sum_list(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum_list(list[1:])

print(f"The sum of the list is {sum_list(list)}") #print the sum of the list