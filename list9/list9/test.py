def counting_sort(arr, col_index):
    n = len(arr)
    
    # Find the maximum value in the specified column
    max_val = max(row[col_index] for row in arr)
    
    # Initialize count array
    count = [0] * (max_val + 1)
    
    # Count the occurrences of each element in the column
    for row in arr:
        count[row[col_index]] += 1
    
    # Calculate the cumulative count array
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Initialize the sorted array
    sorted_arr = [[0] * len(arr[0]) for _ in range(n)]
    
    # Build the sorted array by iterating in reverse order
    for i in range(n - 1, -1, -1):
        value = arr[i][col_index]
        count[value] -= 1
        sorted_arr[count[value]] = arr[i]
    
    return sorted_arr

if __name__ == "__main__":
    array = [[4, 2, 9],
         [1, 5, 6],
         [3, 2, 0],
         [2, 1, 3]]

    sorted_array = counting_sort(array, 0)  # Sort by the second column

    for row in sorted_array:
        print(row)

