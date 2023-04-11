def partitionString(s):
    """
    :type s: str
    :rtype: int
    """

    # one approach
    # go char by char, creating new list of chars if char in list; for example
    #  "abbcccd" -> ["a"], ["ab"], ["ab", "b"], ["abc", "b"], ["abc", "bc"], ["abc", "bc", "c"], ["abcd", bc", "c"]
    partition_string = [[]] * len(s)
                
    # try to remove s one at a time
    s = list(s)
    while s:
        for string in partition_string:
            if s[0] not in string:
                string.append(s[0])
                s = s[1:]
                print(partition_string)
                break
                
    # filter out empty strings
    partition_string = list(filter(None, partition_string))
        
    print(partition_string)
    return len(partition_string)

print(partitionString("abc"))