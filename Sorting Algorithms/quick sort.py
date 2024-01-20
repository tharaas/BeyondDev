# Implement the quick sort algorithm.


def quickSort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array)//2]

    left = []
    equal, right = [], []
    for x in array:
        if x == pivot:
            equal.append(x)
        elif x > pivot:
            right.append(x)
        else:
            left.append(x)

    return quickSort(left) + equal + quickSort(right)


arr = [2, 92, 30, 65, 32, 5, 26, 0]
print("Original Array:", arr)
print("\nQuick Sort")
print(quickSort(arr))
