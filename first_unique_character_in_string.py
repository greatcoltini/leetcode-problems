class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # create our two lists
        unique = []
        non_unique = []

        # for each element in string, we determine its uniqueness
        for c in s:
            if c in non_unique:
                pass
            elif c in unique:
                non_unique.append(c)
                unique.remove(c)
            else:
                unique.append(c)

        # we return the first non-repeating character
        if unique:
            return s.index(unique[0])
        else:
            return -1