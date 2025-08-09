# --------> Maximum Circular Subarray Sum <------------
# Problem Statement: Given a circular array arr[], find the maximum sum of any non-empty subarray. A circular array allows wrapping from the end back to the beginning.
# Note: A subarray may wrap around the end and continue from the beginning, forming a circular segment.

# Examples:
# Input: arr[] = [8, -8, 9, -9, 10, -11, 12]
# Output: 22
# Explanation: The circular subarray [12, 8, -8, 9, -9, 10] gives the maximum sum, which is 22.

# Input: arr[] = [4, -1, -2, 3]
# Output: 7
# Explanation: The circular subarray [3, 4] gives the maximum sum of 7.

# Input: arr[] = [5, -2, 3, 4]
# Output: 12
# Explanation: The circular subarray [3, 4, 5] gives the maximum sum of 12.


def maxCircularSum(arr):

    totalSum = 0
    currMaxSum = 0
    currMinSum = 0
    maxSum = arr[0]
    minSum = arr[0]

    for i in range(len(arr)):

        # Kadane's to find maximum sum subarray
        currMaxSum = max(currMaxSum + arr[i], arr[i])
        maxSum = max(maxSum, currMaxSum)

        # Kadane's to find minimum sum subarray
        currMinSum = min(currMinSum + arr[i], arr[i])
        minSum = min(minSum, currMinSum)

        # Sum of all the elements of input array
        totalSum += arr[i]

    normalSum = maxSum
    circularSum = totalSum - minSum

    # If the minimum subarray is equal to total Sum
    # then we just need to return normalSum
    if minSum == totalSum:
        return normalSum

    return max(normalSum, circularSum)


if __name__ == "__main__":
    arr = [8, -8, 9, -9, 10, -11, 12]
    result = maxCircularSum(arr)
    print("Input Array: ", arr)
    print("Output: ", result)  # Output: 22
