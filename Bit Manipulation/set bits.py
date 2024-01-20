# Write a program to find the number of set bits in a given integer using bit manipulation.


def set_bit(number):
    return bin(number).count("1")


num = int(input("Please enter a positive "))
if num < 0:
    exit(-1)
print("the number of the set bit for ", num, " is ", set_bit(num))
