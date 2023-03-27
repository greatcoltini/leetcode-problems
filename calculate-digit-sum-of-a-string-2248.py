class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # divide the string into groups of size 'k'
        # calculate digit sum of each group
        # we now continue to sum through this the same way; reducing
        # while len(s) > k:
        #     self.individualGroup(s, k)
        print(self.individualGroup(s, k))

    def individualGroup(self, s, k):
        # split into chunks of s
        chunks = [str[i:i+k] for i in range(0, len(s), k)]
        s = ""
        # calculate the digit sum of each group
        digit_sum = 0
        for i in range(0, len(chunks)):
            for j in range(0, len(chunks[i])):
                digit_sum = digit_sum + chunks[i][j]
            s += digit_sum
            digit_sum = 0
