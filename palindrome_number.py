class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # create string of int, and reverse it
        s_x = str(x)
        r_s_x = s_x[::-1]

        # compare reverse string to original string; if difference we break
        for i in range(0, len(s_x)):
            char = s_x[i]
            r_char = r_s_x[i]
            if not char == r_char:
                return False
        return True
