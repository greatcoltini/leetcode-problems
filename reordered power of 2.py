from itertools import permutations


class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        list_num_str = list(str(n))

        # for each digit, we are going to create an int with that digit as the leading,
        # and
        for comb in permutations(list_num_str):
            if comb[0] == '0':
                pass
            else:
                check_num = ""
                for item, value in enumerate(comb):
                    check_num += str(value)
                if self.powerOf2(int(check_num)):
                    return True
        return False


    def powerOf2(self, n):
        """
        :type n: int
        :rtype: bool

        FUNCTION WILL RETURN TRUE IF PROVIDED INT IS POWER OF 2
        """
        return (n != 0) and ((n & (n-1)) == 0)


print(Solution().powerOf2(4))

print(Solution().reorderedPowerOf2(561))