"""
📌 Bucket Sort Algorithm

🔹 High-Level Overview:
   - Bucket Sort is a **distribution-based sorting algorithm** that divides elements into several "buckets" and then sorts each bucket individually.
   - It is particularly useful when sorting floating-point numbers or numbers that are **uniformly distributed** (have an equal chance of occuring)

🔹 How It Works:
   1. **Create empty buckets** based on the number of elements.
   2. **Distribute elements** into the appropriate buckets based on their values.
   3. **Sort each bucket** individually (usually using another sorting algorithm like Insertion Sort or Python's Timsort).
   4. **Concatenate all sorted buckets** to form the final sorted array.

🔹 Time Complexity Analysis:
   - **Best Case:** O(n) (if elements are evenly distributed and sorting within buckets is efficient)
   - **Average Case:** O(n + k) (where `k` is the number of buckets)
   - **Worst Case:** O(n^2) (if all elements fall into the same bucket and sorting is O(n^2))

🔹 Space Complexity:
   - **O(n + k)** (O(n) for input and O(k) for buckets)

✅ Best Used For:
    - Sorting floating-point numbers
    - Uniformly distributed data
    - Cases where another efficient sorting method (like Insertion Sort) can be used within small buckets
"""

def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Step 1: Create empty buckets
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    # Step 2: Insert elements into their respective buckets
    max_value = max(arr)
    for num in arr:
        index = int((num / (max_value + 1)) * bucket_count)  # produce num between 0 and 1 and scale up by multiplying by bucket count, adding 1 prevents index OOB for max_val
        buckets[index].append(num)

    # Step 3: Sort each bucket individually
    for bucket in buckets:
        bucket.sort()

    # Step 4: Concatenate all sorted buckets into a single array
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

# Example Input
arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]

# Sorting using Bucket Sort
sorted_arr = bucket_sort(arr)

# Output
print("Original Array:", arr)
print("Sorted Array:", sorted_arr)
