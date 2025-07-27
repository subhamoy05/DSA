# --------------> Move all zero to end of the array <-----------------

# Note: Given an array of integers,The task is to move all zeroes to the end of the array while maintaining the relative order of all non-zero elements.


# Example: arr[] = {0, 1, 0, 3, 12}
# Output: {1, 3, 12, 0, 0}
# Explanation: There are two zeroes that are moved to the end.


def move_zeroes(arr):
    if not arr:
        return arr
    # Pointer to track the position for next non-zero element
    count = 0

    for i in range(len(arr)):

        # if the current element is non-zero
        if arr[i] != 0:

            # Swap the current element with the 0 at index 'count'
            arr[i], arr[count] = arr[count], arr[i]

            # Move count pointer to the next position
            count += 1


if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    result = move_zeroes(arr)
    print("Input Array : ", arr)
    print("Output Array : ", end="")
    for num in arr:
        print(num, end=" ")
