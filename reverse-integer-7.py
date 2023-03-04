class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reversed_int = ""

        if x < 0:
            reversed_int += "-"

        x = abs(x)

        while x > 0:
            reversed_int += str(x % 10)
            x = x // 10

        if reversed_int == "" or (int(reversed_int) > (pow(2, 31) - 1)) or (int(reversed_int) < (pow(-2, 31))):
            return 0

        return int(reversed_int)