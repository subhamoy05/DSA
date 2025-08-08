# -----------> Maximum Product Subarray <------------

# Problem Statement: Given an array arr[] consisting of positive, negative, and zero values, find the maximum product that can be obtained from any contiguous subarray of arr[].

# Examples:
# Input: arr[] = [-2, 6, -3, -10, 0, 2]
# Output: 180
# Explanation: The subarray with maximum product is [6, -3, -10] with product = 6 * (-3) * (-10) = 180.

# Input: arr[] = [-1, -3, -10, 0, 6]
# Output: 30
# Explanation: The subarray with maximum product is [-3, -10] with product = (-3) * (-10) = 30.

# Input: arr[] = [2, 3, 4] 
# Output: 24 
# Explanation: For an array with all positive elements, the result is product of all elements.

def maxProduct(arr):

    n = len(arr)

    # max product ending at the current index
    currMax = arr[0]

    # min product ending at the current index
    currMin = arr[0]

    # Initialize overall max product
    maxProd = arr[0]

    # Iterate through the array
    for i in range(1, n):

        # Temporary variable to store the maximum product ending
        # at the current index
        temp = max(arr[i], arr[i] * currMax, arr[i] * currMin)

        # Update the minimum product ending at the current index
        currMin = min(arr[i], arr[i] * currMax, arr[i] * currMin)

        # Update the maximum product ending at the current index
        currMax = temp

        # Update the overall maximum product
        maxProd = max(maxProd, currMax)

    return maxProd


if __name__ == "__main__":
    arr = [-2, 6, -3, -10, 0, 2]
    result = maxProduct(arr)
    print("Input Array: ", arr)
    print("Output: ", result)