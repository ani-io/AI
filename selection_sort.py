def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the minimum is at position i
        min_index = i
        
        # Greedy choice: find the minimum element in the unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Driver code
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Original array:", arr)
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)
