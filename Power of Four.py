class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # change to float so we can use decimal values
        i = float(n)

        # loop through until we reach n value less than 4
        while i >= 4:
            i = i / 4

        # if we have 1 we know it is divisible, else not
        if i == 1:
            return True
        else:
            return False