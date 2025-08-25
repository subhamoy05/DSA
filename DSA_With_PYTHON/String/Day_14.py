# --------------> String to Integer - Write your own atoi() <--------------

# Problem Statement: Given a string s, convert it into integer format without utilizing any built-in functions. Refer the below steps to know about atoi() function.
# Skip any leading whitespaces.
# Check for a sign (‘+’ or ‘-‘), default to positive if no sign is present.
# Read the integer by ignoring leading zeros until a non-digit character is encountered or end of the string is reached. If no digits are present, return 0.
# If the integer is greater than 231 – 1, then return 231 – 1 and if the integer is smaller than -231, then return -231.
# Examples:

# Input: s = "-123"
# Output: -123

# Input: s = "   -"
# Output: 0
# Explanation: No digits are present, therefore 0.

# Input: s = "  1231231231311133"
# Output: 2147483647
# Explanation: The converted number is greater than 231 - 1, therefore print 231 - 1 = 2147483647.

# Input: s = "-999999999999"
# Output: -2147483648
# Explanation: The converted number is smaller than -231, therefore print -231 = -2147483648.

# Input: s = "  -0012gfg4"
# Output: -12
# Explanation: Nothing is read after -12 as a non-digit character 'g' was encountered.

def myAtoi(s):
    sign = 1
    res = 0
    idx = 0
    n = len(s)

    # Ignore leading whitespaces
    while idx < n and s[idx] == ' ':
        idx += 1

    # Store the sign of number
    if idx < n and (s[idx] == '+' or s[idx] == '-'):
        if s[idx] == '-':
            sign = -1
        idx += 1

    # Construct the number digit by digit
    while idx < n and '0' <= s[idx] <= '9':
        digit = ord(s[idx]) - ord('0')
        res = 10 * res + digit

        # Handle overflow and underflow
        if res > 2**31 - 1:
            return (2**31 - 1) if sign == 1 else -2**31

        idx += 1

    return res * sign

if __name__ == "__main__":
    s = "-123"
    result = myAtoi(s)
    print("Input String: ", s)
    print("Output: ", result)  # Output: -123

    s = "   -"
    result = myAtoi(s)
    print("Input String: ", s)
    print("Output: ", result)  # Output: 0

    s = "  1231231231311133"
    result = myAtoi(s)
    print("Input String: ", s)
    print("Output: ", result)  # Output: 2147483647

    s = "-999999999999"
    result = myAtoi(s)
    print("Input String: ", s)
    print("Output: ", result)  # Output: -2147483648

    s = "  -0012gfg4"
    result = myAtoi(s)
    print("Input String: ", s)
    print("Output: ", result)  # Output: -12