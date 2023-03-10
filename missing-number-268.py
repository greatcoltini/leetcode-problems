# 268 missing number
# very brute force approach
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        first = nums[0]
        if (nums[0] != 0):
            return 0
        for num in nums[1:]:
            if num != first + 1:
                return first + 1
            first = num
        return nums[-1] + 1