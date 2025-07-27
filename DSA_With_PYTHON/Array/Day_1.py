# -------------> Find a Second Largest Element in an array <-----------------

# Note : If the second largest element does not exist, return -1, and The second largest element should be equal to the largest element.

# Example: arr[] = {12, 35, 1, 10, 34, 1}
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.

def second_largest(arr):
    if len(arr) < 2:
        return -1
    
    first = second = float('-inf')
    
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    
    return second if second != float('-inf') else -1

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    result = second_largest(arr)
    print("Input Array : " ,arr)
    print("Output : ", result)  # Output: 34