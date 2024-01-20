# Write a program to check if a given number is even or odd using bit manipulation.


def check_odd_even(number):
    if number ^ 1 == number+1:
        return True
    return False


print("if the number 65 is even? ",check_odd_even(65))
print("if the number 54 is even? ",check_odd_even(54))
