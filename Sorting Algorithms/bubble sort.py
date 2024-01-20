# Implement the bubble sort algorithm.


def bubble_sort(array):
    temp = array[0]
    for index in range(len(array)):
        for index2 in range(len(array)-index-1):
            if array[index2] > array[index2+1]:
                temp = array[index2]
                array[index2] = array[index2+1]
                array[index2+1] = temp
    return array


arr = [2, 92, 30, 65, 32, 5, 26, 0]
print("Bubble Sort")
print(arr)
print(bubble_sort(arr))
