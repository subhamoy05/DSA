# ------------> Minimize the maximum difference between the heights <------------

# Problem Statement: Given the heights of n towers and a positive integer k, increase or decrease the height of all towers by k (only once). After modifications, the task is to find the minimum difference between the heights of the tallest and the shortest tower.

# Examples:
# Input: arr[] = [12, 6, 4, 15, 17, 10], k = 6
# Output: 8
# Explanation: Update arr[] as [12 - 6, 6 + 6, 4 + 6, 15 - 6, 17 - 6, 10 - 6] = [6, 12, 10, 9, 11, 4]. Now, the minimum difference is 12 - 4 = 8.

# Input: arr[] = [1, 5, 10, 15], k = 3
# Output: 8
# Explanation: Update arr[] as [1 + 3, 5 + 3, 10 - 3, 15 - 3] = [4, 8, 7, 12]. Now, the minimum difference is 8.

# Python program to minimize the maximum difference
# between heights using Sorting

def getMinDiff(arr, k):
    n = len(arr)
    arr.sort()

    # If we increase all heights by k or decrease all
    # heights by k, the result will be arr[n - 1] - arr[0]
    res = arr[n - 1] - arr[0]

    # For all indices i, increment arr[0...i-1] by k and
    # decrement arr[i...n-1] by k
    for i in range(1, len(arr)):
        # Impossible to decrement height of ith tower by k, 
        # continue to the next tower
        if arr[i] - k < 0:
            continue

        # Minimum height after modification
        minH = min(arr[0] + k, arr[i] - k)

        # Maximum height after modification
        maxH = max(arr[i - 1] + k, arr[n - 1] - k)

        # Store the minimum difference as result
        res = min(res, maxH - minH)
    
    return res

if __name__ == "__main__":
    arr = [12, 6, 4, 15, 17, 10]
    k = 6
    result = getMinDiff(arr, k)
    print("Input Array: ", arr)
    print("k: ", k)
    print("Output: ", result)  # Output: 8