def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """

    len_substring = 0
    current_highest = 0
    un_unique = []

    for char in s:

        # traverse until non-unique char
        if char not in un_unique:
            len_substring += 1
            un_unique.append(char)
        # once we have a non-unique char, we set this as a substring
        # and continue traversing the string
        else:
            if len_substring > current_highest:
                current_highest = len_substring
            un_unique = [char]

            # reset the un_unique counter and continue from this letter...
            len_substring = 1

    # return the highest substring

    if current_highest < len_substring:
        current_highest = len_substring

    return current_highest

print(lengthOfLongestSubstring("dvdf"))

def alt_lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """

    len_substring = 0
    current_highest = 0
    un_unique = []
    counter = 0
    start_point = 0

    for char in s:



    # return the highest substring

    if current_highest < len_substring:
        current_highest = len_substring

    return current_highest



print(alt_lengthOfLongestSubstring("dvdf"))
print(alt_lengthOfLongestSubstring("aab"))
print(alt_lengthOfLongestSubstring("abcaabc"))
