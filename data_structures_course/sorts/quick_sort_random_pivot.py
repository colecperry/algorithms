import random, time

def quick_sort_random(arr, l, r):
    if l < r:
        q = partition_random(arr, l, r)
        quick_sort_random(arr, l, q - 1)
        quick_sort_random(arr, q + 1, r)

def partition_random(arr, l, r):
    pivot_index = random.randint(l, r)  # Select a random pivot
    arr[pivot_index], arr[r] = arr[r], arr[pivot_index]  # Swap with last element
    pivot = arr[r]

    i = l - 1
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


# Run randomized pivot QuickSort on sorted list
arr2 = [4, 6, 3, 7, 5]

start_time = time.time()
quick_sort_random(arr2, 0, len(arr2) - 1)
end_time = time.time()

print("Randomized Pivot QuickSort Time:", end_time - start_time)
