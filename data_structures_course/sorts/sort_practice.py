def bubble_sort_backwards(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort_backwards([4, 3, 2, 1]))


def bubble_sort_forwards(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr



print(bubble_sort_forwards([4, 3, 2, 1]))


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


print(selection_sort([4, 3, 2, 1]))


def insertion_sort(arr):
    for i in range(1, len(arr)):
        counter = i
        while counter > 0 and arr[counter] < arr[counter - 1]:
            arr[counter], arr[counter - 1] = arr[counter - 1], arr[counter]
            counter = counter - 1
    return arr

print(insertion_sort([4, 3, 2, 1]))





