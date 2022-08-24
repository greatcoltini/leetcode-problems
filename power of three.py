import numpy as np
import re

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # match with regex
        base_three = np.base_repr(n, 3)
        return re.match(("^10*$"), base_three)

