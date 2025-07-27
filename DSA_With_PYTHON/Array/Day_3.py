# -----------------> Reverse an array <-----------------


# Note : Given an array arr[], the task is to reverse the array. Reversing an array means rearranging the elements such that the first element becomes the last, the second element becomes second last and so on.

# Example: Input: arr[] = {1, 4, 3, 2, 6, 5}  
# Output: {5, 6, 2, 3, 4, 1}
# Explanation: The first element 1 moves to last position, the second element 4 moves to second-last and so on.

def reverse_array(arr):

    #Initialize left to the beginning and right to the end of the array
    left = 0
    right = len(arr) - 1

    #Iterate till left is less than right
    while left < right :

        #Swap the elements at left and right position
        arr[left], arr[right] = arr[right], arr[left]

        #Increment the left pointer
        left += 1

        #Decrement the right pointer
        right -= 1

if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]
    reverse_array(arr)
    print("Input Array : ", arr)
    print("Reversed Array : ", end="")
    for num in arr:
        print(num, end=" ")  # Output: 5 6 2 3 4 1