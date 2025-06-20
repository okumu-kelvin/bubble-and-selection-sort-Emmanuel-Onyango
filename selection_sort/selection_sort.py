# Function to find the index of the smallest element
def MIN(arr, start, n):
    smallest = arr[start]
    pos = start
    for j in range(start + 1, n):
        if arr[j] < smallest:
            smallest = arr[j]
            pos = j
    return pos  # Correctly return position

# Main selection sort function
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        pos = MIN(arr, i, n)
        arr[i], arr[pos] = arr[pos], arr[i]
    # No need to return arr if modifying in-place, but let's return it anyway
    return arr

# Testing the function
my_array = [29, 10, 14, 37, 13]
sorted_array = selection_sort(my_array)  # Now this has a return value
print("Sorted array:", sorted_array)
