print("Ashutosh Kumar")
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Sample list to be sorted
arr = [64, 34, 25, 12, 22, 11, 90]

# Call the bubble_sort function
bubble_sort(arr)

# Print the sorted array
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")