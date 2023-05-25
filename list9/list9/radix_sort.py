def counting_sort(arr, col_index):
    n = len(arr)
    
    # Find the maximum value in the specified column
    max_val = max(row[col_index] for row in arr)
    
    count = [0] * (max_val + 1)
    
    # Count the occurrences of each element in the column
    for row in arr:
        count[row[col_index]] += 1
    
    # Calculate the cumulative count array [C}]
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    sorted_arr = [[0] * len(arr[0]) for _ in range(n)]
    
    # Build the sorted array
    for i in range(n - 1, -1, -1):
        value = arr[i][col_index]
        count[value] -= 1
        sorted_arr[count[value]] = arr[i]
    
    return sorted_arr

def radix_sort(arr):
    for i in range(len(arr)-1, -1, -1):
        arr = counting_sort(arr, i)
    return arr

if __name__ == "__main__":
    # arr = [4, 2, 2, 8, 3, 3, 1]
    # arr =  [[1, 2, 7],
    #         [7, 8, 8],
    #         [4, 5, 9]]
    # sorted_arr = counting_sort(arr, 0)
    # print(sorted_arr)

    # arr = [[5, 3, 9, 2, 7],
    #        [2, 4, 6, 1, 8],
    #        [9, 1, 5, 4, 6]]

    arr = [[5, 3, 9, 2, 7],
           [5, 1, 9, 2, 7],
           [5, 1, 9, 1, 8],
           [9, 1, 5, 4, 6]]
    print(radix_sort(arr))
