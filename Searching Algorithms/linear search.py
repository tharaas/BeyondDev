# Implement the linear search algorithm.


def linear_search(array, value):
    for index in range(len(array)):
        if array[index] == value:
            return index
    return None


arr2 = [36, 85, 71, 44, 10]
print("the index of number 44 in new array is", linear_search(arr2, 44))
