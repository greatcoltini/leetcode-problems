class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # split string by spaces
        split_string = s.split()

        return len(split_string[-1])