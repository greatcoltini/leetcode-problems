class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        numbers_str = ""

        for digit in digits:
            numbers_str += str(digit)

        print(numbers_str)

        return numbers_str