# Write a program to calculate the factorial of a number using recursion.


def factorial(number):
    if number == 1:
        return number
    return number * factorial(number-1)


num = int(input("Please enter a number "))
print('The factorial of number ', num, ' is ', factorial(num))
