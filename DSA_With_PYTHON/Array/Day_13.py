# ---------------> Smallest Missing Positive Number <---------------
# Problem statement: Given an unsorted array arr[] with both positive and negative elements, find the smallest positive number missing from the array.

# Examples:
# Input: arr[] = [2, -3, 4, 1, 1, 7]
# Output: 3
# Explanation: 3 is the smallest positive number missing from the array.

# Input: arr[] = [5, 3, 2, 5, 1]
# Output: 4
# Explanation: 4 is the smallest positive number missing from the array.

# Input: arr[] = [-8, 0, -1, -4, -3]
# Output: 1 
# Explanation: 1 is the smallest positive number missing from the array.

def missingNumber(arr):
    n = len(arr)
    flag = False

    # Check if 1 is present in array or not
    for i in range(n):
        if arr[i] == 1:
            flag = True
            break

    # If 1 is not present
    if not flag:
        return 1

    # Change out of range values to 1
    for i in range(n):
        if arr[i] <= 0 or arr[i] > n:
            arr[i] = 1

    # Mark the occurrence of numbers 
    # directly within the same array
    for i in range(n):
        arr[(arr[i] - 1) % n] += n

    # Finding which index has value less than n
    for i in range(n):
        if arr[i] <= n:
            return i + 1

    # If array has values from 1 to n
    return n + 1

if __name__ == "__main__":
    arr = [2, -3, 4, 1, 1, 7]
    result = missingNumber(arr)
    print("Input Array: ", arr)
    print("Output: ", result)  # Output: 3

    arr = [5, 3, 2, 5, 1]
    result = missingNumber(arr)
    print("Input Array: ", arr)
    print("Output: ", result)  # Output: 4

    arr = [-8, 0, -1, -4, -3]
    result = missingNumber(arr)
    print("Input Array: ", arr)
    print("Output: ", result)  # Output: 1