import random
import time

def quick_sort_deterministic(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_deterministic(arr, low, pi - 1)
        quick_sort_deterministic(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as pivot
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_randomized(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        quick_sort_randomized(arr, low, pi - 1)
        quick_sort_randomized(arr, pi + 1, high)

def randomized_partition(arr, low, high):
    random_index = random.randint(low, high)  # Randomly selecting a pivot
    arr[random_index], arr[high] = arr[high], arr[random_index]  # Swapping pivot with last element
    return partition(arr, low, high)

# Input from user
input_array = input("Enter the elements of the array separated by spaces: ")
arr = list(map(int, input_array.split()))

# Deterministic Quick Sort
det_arr = arr.copy()  # Copy to preserve original array
start_time_deterministic = time.time()
quick_sort_deterministic(det_arr, 0, len(det_arr) - 1)
end_time_deterministic = time.time()
det_time = end_time_deterministic - start_time_deterministic

# Randomized Quick Sort
rand_arr = arr.copy()  # Copy to preserve original array
start_time_randomized = time.time()
quick_sort_randomized(rand_arr, 0, len(rand_arr) - 1)
end_time_randomized = time.time()
rand_time = end_time_randomized - start_time_randomized

# Output results
print(f"Sorted array using deterministic Quick Sort: {det_arr}")
print(f"Time taken (deterministic): {det_time:.6f} seconds")

print(f"Sorted array using randomized Quick Sort: {rand_arr}")
print(f"Time taken (randomized): {rand_time:.6f} seconds")
