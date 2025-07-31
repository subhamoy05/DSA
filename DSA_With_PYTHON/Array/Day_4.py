
# --------------> Rotate Array <--------------

# Note : Given an unsorted array arr[] , Rotate the array to the left (Counter Clockwise direction) by d steps. Where d is a positive integer. Do the mentioned change in the array in-place

# Example 1: Input: arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
# Output: {3, 4, 5, 6, 7, 1, 2}
# Explanation: When the rotated by 2 elements, it become {3, 4, 5, 6, 7, 1, 2}

# Example 2: Input: arr[] = {7, 3, 9, 1}, d = 9
# Output: {3, 9, 1, 7}
# Explanation: When we rotate 9 times, we'll ger 3, 9, 1, 7 as resultant array

# -----------------------------> Juggling Algorithm <-----------------------------

# import math


# # Function to rotate array
# def RotateArr(arr, d):
#     n = len(arr)

#     # Handle the case where d > size of array
#     d %= n

#     # Calculate the number of cycles in the rotation
#     cycles = math.gcd(n, d)

#     # Process each cycle
#     for i in range(cycles):

#         # Start element of the current cycle
#         startElement = arr[i]

#         # Start index of current cycle
#         currIdx = i

#         # Rotate elements till we reach the start of cycle
#         while True:
#             nextIdx = (currIdx + d) % n

#             if nextIdx == i:
#                 break

#             # Updata the next index with the current element
#             arr[currIdx] = arr[nextIdx]
#             currIdx = nextIdx

#             # Copy the start element of current cycle at the last
#             # index of the cycle

#             arr[currIdx] = startElement


# if __name__ == "__main__":
#     arr = [1, 2, 3, 4, 5, 6, 7]
#     d = 3
#     RotateArr(arr, d)
#     print("Input Array : ", arr)
#     print("Rotated Array : ", end="")
#     for num in arr:
#         print(num, end=" ")  # Output: 3 4 5 6 7 1 2


# ------------------> Reversal Algorithm <-----------------


def rotateArray(arr, d):
    n = len(arr)

    # Handle the case where d > size of array
    d %= n

    # Reverse the first part of the array
    reverseArray(arr, 0, d - 1)

    # Reverse the second part of the array
    reverseArray(arr, d, n - 1)

    # Reverse the entire array
    reverseArray(arr, 0, n - 1)


# This function reverses the elements of the array from start to end
def reverseArray(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# --------------> Rotate Array <--------------

# Note : Given an unsorted array arr[] , Rotate the array to the left (Counter Clockwise direction) by d steps. Where d is a positive integer. Do the mentioned change in the array in-place

# Example 1: Input: arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
# Output: {3, 4, 5, 6, 7, 1, 2}
# Explanation: When the rotated by 2 elements, it become {3, 4, 5, 6, 7, 1, 2}

# Example 2: Input: arr[] = {7, 3, 9, 1}, d = 9
# Output: {3, 9, 1, 7}
# Explanation: When we rotate 9 times, we'll ger 3, 9, 1, 7 as resultant array

import math

#Function to rotate array
def RotateArr(arr, d):
    n = len(arr)

    # Handle the case where d > size of array
    d %= n

    # Calculate the number of cycles in the rotation 
    cycles = math.gcd(n, d)

    # Process each cycle
    for i in range(cycles):

        # Start element of the current cycle
        startElement = arr[i]

        # Start index of current cycle
        currIdx = i

        # Rotate elements till we reach the start of cycle
        while True:
            nextIdx = (currIdx + d) % n

            if nextIdx == i:
                break

            # Updata the next index with the current element
            arr[currIdx] = arr[nextIdx]
            currIdx = nextIdx

            # Copy the start element of current cycle at the last
            # index of the cycle

            arr[currIdx] = startElement

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 3
    RotateArr(arr, d)
    print("Input Array : ", arr)
    print("Rotated Array : ", end="")
    for num in arr:
        print(num, end=" ")  # Output: 3 4 5 6 7 1 2

