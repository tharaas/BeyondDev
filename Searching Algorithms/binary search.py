# Implement the binary search algorithm.


def binary_search(array, value, left, right):
    if left > right:
        return -1

    middle = int((left + right)/2)
    if array[middle] == value:
        return middle
    elif array[middle] > value:
        return binary_search(array, value, left, middle - 1)
    else:
        return binary_search(array, value, middle + 1, right)


arr2 = [36, 85, 71, 44, 10, 64, 98, 24]
arr2.sort()
print(arr2)
print("the index of number 44 in new array is", binary_search(arr2, 44, 0, len(arr2)))
