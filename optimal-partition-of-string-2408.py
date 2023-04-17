def partitionString(s):
    """
    :type s: str
    :rtype: int
    """

    # one approach
    # go char by char, creating new list of chars if char in list; for example
    #  "abbcccd" -> ["a"], ["ab"], ["ab", "b"], ["abc", "b"], ["abc", "bc"], ["abc", "bc", "c"], ["abcd", bc", "c"]
    partition_string = []
                
    # try to remove s one at a time
    s = list(s)
    while s:
        letter = s[0]
        if partition_string:
            for string in partition_string:
                if letter not in string:
                    string += letter
                    letter = None
                    s = s[1:]
                    print(partition_string)
                    break
        else:
            partition_string.append(letter)
            s = s[1:]
                
    # filter out empty strings
    partition_string = list(filter(None, partition_string))
        
    print(partition_string)
    return len(partition_string)

def partitionStringV2(string):
    # we want to take in string; repeat number of unique compositions
    
    #  approach: parse through string, and create list of lists
    #  if character is in first list, we move to next, else, add it
    #  return length of lists for number of unique lists created
    partitioned_string = [[]] * 1000
    entered = False
    counter = 0 
    for char in string:
        counter = 0
        entered = False
        # loop through partitioned string until we have entered this char
        while not entered:
            if not partitioned_string[counter]:
                partitioned_string[counter].append(char)
                entered = True
                
            # if the partitioned string exists, look inside
            if partitioned_string[counter]:
                
                if char not in partitioned_string[counter]:
                    partitioned_string[counter].append(char)
                    entered = True
                    
            # partitioned string does not exist, therefore add char
            else:
                partitioned_string[counter].append(char)
                entered = True
            counter += 1
    return len(partitioned_string)                      
        

print(partitionStringV2("abcbc"))