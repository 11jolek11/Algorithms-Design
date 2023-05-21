import numpy as np


# def countingSortForRadix(inputArray, placeValue):
#     # We can assume that the number of digits used to represent
#     # all numbers on the placeValue position is not greater than 10
#     uni = len(np.unique(inputArray))
#     countArray = [0] * uni 
#     inputSize = len(inputArray)

#     # placeElement is the value of the current place value
#     # of the current element, e.g. if the current element is
#     # 123, and the place value is 10, the placeElement is
#     # equal to 2
#     for i in range(inputSize):
#         placeElement = (inputArray[i] // placeValue) % 10
#         countArray[placeElement] += 1

#     for i in range(1, 10):
#         countArray[i] += countArray[i-1]

#     # Reconstructing the output array
#     outputArray = [0] * inputSize
#     i = inputSize - 1
#     while i >= 0:
#         currentEl = inputArray[i]
#         placeElement = (inputArray[i] // placeValue) % 10
#         countArray[placeElement] -= 1
#         newPosition = countArray[placeElement]
#         outputArray[newPosition] = currentEl
#         i -= 1

#     return outputArray


# def radixSort(inputArray):
#     # Step 1 -> Find the maximum element in the input array
#     maxEl = max(inputArray)

#     # Step 2 -> Find the number of digits in the `max` element
#     D = 1
#     while maxEl > 0:
#         maxEl /= 10
#         D += 1

#     # Step 3 -> Initialize the place value to the least significant place
#     placeVal = 1

#     # Step 4
#     outputArray = inputArray
#     while D > 0:
#         outputArray = countingSortForRadix(outputArray, placeVal)
#         placeVal *= 10
#         D -= 1

#     return outputArray

# # input = [2,20,61,997,1,619]

# input = [
#     [1, 2, 3],
#     [7, 8, 9],
#     [4, 5, 6],
#     ]

# # input = [
# #     [1, 2, 3],
# #     [4, 8, 9],
# #     [4, 5, 6],
# #     ]

# print(input)
# sorted = radixSort(input)
# print(sorted)


# def counting_sort(arr: np.ndarray, max_value, index: int):
#     count = [0] * (max_value + 1)
#     # output = [0] * len(arr)
#     output = np.zeros(arr.shape)

#     for num in arr[:, index]:
#         count[num] += 1

#     for i in range(1, max_value + 1):
#         count[i] += count[i - 1]

#     for i in range(len(arr) - 1, -1, -1):
#         # FIXME: 
#         # num = arr[:, index][i]
#         # output[count[num] - 1][index] = num
#         # count[num] -= 1






#         # num = arr[:, i]
#         # output[count[num[index]] - 1] = num
#         # count[num[index]] -= 1
#         pass

#     return output

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
    arr = [[5, 3, 9, 2, 7],
           [2, 4, 6, 1, 8],
           [9, 1, 5, 4, 6]]
    print(radix_sort(arr))
