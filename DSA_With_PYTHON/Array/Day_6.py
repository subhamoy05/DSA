# ------------------> Majority Element <------------------

# Note: You are given an array ar[] consisting of n integers where each number represent a vote to a candidate, Return the candidates that have votes greater then [n/3], if there's not a majority vote, return an empty array.
# The answer should be returned in an increasing format.

# Examples:
# Input: arr[] = [2, 2, 3, 1, 3, 2, 1, 1]
# Output: [1, 2]
# Explanation: The frequency of 1 and 2 is 3, which is more than floor n/3 (8/3 = 2).

# Input: arr[] = [-5, 3, -5]
# Output: [-5]
# Explanation: The frequency of -5 is 2, which is more than floor n/3 (3/3 = 1).

# Input: arr[] = [3, 2, 2, 4, 1, 4]
# Output: [ ]
# Explanation: There is no majority element.


def majority_Element(arr):
    n = len(arr)

    # Initialize two candidates and their counts
    candidate1, candidate2 = -1, -1
    count1, count2 = 0, 0

    for element in arr:
        # Increment count for candidate 1
        if candidate1 == element:
            count1 += 1
        # Increment count for candidate 2
        elif candidate2 == element:
            count2 += 1
        # New candidate 1 if count is Zero
        elif count1 == 0:
            candidate1 = element
            count1 += 1
        # New candidate 2 if count is Zero
        elif count2 == 0:
            candidate2 = element
            count2 += 1
        # Decrease counts if neither candidate
        else:
            count1 -= 1
            count2 -= 1

    res = []
    count1, count2 = 0, 0

    # Count the occurrences of candidates
    for element in arr:
        if candidate1 == element:
            count1 += 1
        if candidate2 == element:
            count2 += 1

    # Add to result if they are majority elements
    if count1 > n / 3:
        res.append(candidate1)
    if count2 > n / 3 and candidate1 != candidate2:
        res.append(candidate2)

    if len(res) == 2 and res[0] > res[1]:
        res[0], res[1] = res[1], res[0]

    return res


if __name__ == "__main__":
    arr = [2, 2, 3, 1, 3, 2, 1, 1]
    print("Input Array : ", arr)
    result = majority_Element(arr)
    print("Output Array : ", end="")
    if result:
        for num in sorted(result):
            print(num, end=" ")
    else:
        print("No Majority Element")
