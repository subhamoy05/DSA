# --------------> Check if two Strings are Anagrams of each other <---------------
# Problem Statement: Given two non-empty strings s1 and s2 of lowercase letters, determine if they are anagrams — i.e., if they contain the same characters with the same frequencies.

# Examples:
# Input: s1 = “geeks”  s2 = “kseeg”
# Output: true
# Explanation: Both the string have same characters with same frequency. So, they are anagrams.

# Input: s1 = "allergy", s2 = "allergyy"
# Output: false
# Explanation: Although the characters are mostly the same, s2 contains an extra 'y' character. Since the frequency of characters differs, the strings are not anagrams.

# Input: s1 = "listen", s2 = "lists"
# Output: false
# Explanation: The characters in the two strings are not the same — some are missing or extra. So, they are not anagrams.


def areAnagrams(s1, s2):
    
    if len(s1) != len(s2):
        return False
        
    # for lowercase a-z
    freq = [0] * 26  
    
    # Count frequency of each character in s1
    for ch in s1:
        freq[ord(ch) - ord('a')] += 1

    # Subtract frequency using characters from s2
    for ch in s2:
        freq[ord(ch) - ord('a')] -= 1

    # Check if all frequencies are zero
    for count in freq:
        if count != 0:
            return False
            
    return True

if __name__ == "__main__":
    s1 = "geeks"
    s2 = "kseeg"
    print(areAnagrams(s1, s2))  # Output: True

    s1 = "allergy"
    s2 = "allergyy"
    print(areAnagrams(s1, s2))  # Output: False

    s1 = "listen"
    s2 = "lists"
    print(areAnagrams(s1, s2))  # Output: False