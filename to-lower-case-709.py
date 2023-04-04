class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        # use static list to convert
        new_str = ""

        for char in s:
            # convert to ascii
            intChar = ord(char)

            if intChar > 90:
                new_str += char
            else:
                new_str += chr(intChar + 32)
        return new_str
