# def countingSort(inputArray):
#     # Find the maximum element in the inputArray
#     maxElement = max(inputArray)

#     countArrayLength = maxElement+1

#     # Initialize the countArray with (max+1) zeros
#     countArray = [0] * countArrayLength

#     # Step 1 -> Traverse the inputArray and increase 
#     # the corresponding count for every element by 1
#     for el in inputArray:
#         countArray[el] += 1

#     # Step 2 -> For each element in the countArray, 
#     # sum up its value with the value of the previous 
#     # element, and then store that value 
#     # as the value of the current element
#     for i in range(1, countArrayLength):
#         countArray[i] += countArray[i-1]

#     # Step 3 -> Calculate element position
#     # based on the countArray values
#     outputArray = [0] * len(inputArray)
#     i = len(inputArray) - 1
#     while i >= 0:
#         currentEl = inputArray[i]
#         countArray[currentEl] -= 1
#         newPosition = countArray[currentEl]
#         outputArray[newPosition] = currentEl
#         i -= 1

#     return outputArray

# inputArray = [2,2,0,6,1,9,9,7]
# print("Input array = ", inputArray)

# sortedArray = countingSort(inputArray)
# print("Counting sort result = ", sortedArray)
import numpy as np


# def counting_sort(arr, k):
#     C = np.zeros(k)
#     B = np.zeros(len(arr))
#     # print(C)
#     # print(B)
#     for i in range(len(arr)-1):
#         # print(arr[i])
#         C[arr[i]-1] += 1
#     for i in range(1, len(arr)):
#         C[i] += C[i-1]
#     for i in range(len(arr)-1, -1, -1):
#         B[int(C[arr[i]-1])] = arr[i]
#         # print(B[int(C[arr[i]-1])])
#         # print(arr[i])
#         C[arr[i]-1] -= 1
#         print(C[arr[i]-1])
#     return B

# def counting_sort(arr, max_value):
#     count = [0] * (max_value + 1)
#     output = [0] * len(arr)

#     for num in arr:
#         count[num] += 1

#     for i in range(1, max_value + 1):
#         count[i] += count[i - 1]

#     for i in range(len(arr) - 1, -1, -1):
#         num = arr[i]
#         output[count[num] - 1] = num
#         count[num] -= 1

#     return output
from robots import Table, Robot


def counting_sort(arr, max_value):
    count = [0] * (max_value + 1)
    output = [0] * len(arr)

    # for num in arr:
    #     count[num] += 1
    for num in range(len(arr)):
        count[getattr(arr[num], "robot_range")] += 1

    for i in range(1, max_value + 1):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        # num = arr[i]
        num = getattr(arr[i], "robot_range")
        output[count[num] - 1] = num
        count[num] -= 1

    return output

if __name__ == "__main__":
    # arr = [4, 2, 2, 8, 3, 3, 1]
    # sorted_arr = counting_sort(arr, 8)
    # print(sorted_arr)
    t = Table()
    t.fill(5)
    t.show()
    t.frame = counting_sort(t.frame, 100)
    t.show()

