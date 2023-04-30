class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # we create initial variables, and we find length of smallest string 
        prefix = ""
        parse_amt = len(min(strs, key=len))
        counter = 0
        
        # if our smallest string is 0, we return as there is no common prefix
        if parse_amt == 0:
            return prefix
        else:
            while counter < parse_amt:
                
                # we pull the prefix off the first string, and compare, break if not matching
                if strs[0]:
                    compare_letter = strs[0][counter]
                for string in strs:
                    if not string:
                        return prefix
                    if string[counter] != compare_letter:
                        return prefix
                
                prefix += compare_letter
                counter += 1
        
        return prefix
                    