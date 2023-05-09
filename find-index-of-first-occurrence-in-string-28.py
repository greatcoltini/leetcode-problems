def strStr(haystack, needle):
    """_summary_

    Args:
        haystack (str): string to search in
        needle (str): string to search for
    Return:
        index (int): integer where needle occurs first in the haystack
    """
    # start at index 0 of haystack, search for match with index 0 of needle
    # if we find it, confirm that second index matches, if not skip positions based
    # on index 
    counter = 0
    needle_index = 0
    in_search = False
    search_point = 0
    while counter <= len(haystack) - 1:
        # we have found the sequence if needle_index is equal to the length of the needle
        if needle_index > len(needle) - 1:
            if in_search:
                return counter - len(needle)
            else:
                return -1
            
        # if we have the haystack item equal to the needle item, we are parsing the substring
        if haystack[counter] == needle[needle_index]:
            needle_index += 1
            in_search = True
            # # set our current search point to the counter
            # search_point = counter
        else:
            if in_search:
                # counter = search_point + needle_index - 1
                in_search = False
                needle_index = 0
                
        counter += 1
        
        # account for 1 word edge case
        if counter >= len(haystack) - 1:
            return counter - 1
    
    return -1

# print(strStr("hello world", "wor"))
# print(strStr("leetcode", "leeto"))
# print(strStr("helno there general hello there general", "hell"))
print(strStr("a", "a"))
