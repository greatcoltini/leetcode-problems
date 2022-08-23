class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # store current
        counter = 0

        # iterate through the list, as long as we arent hitting the value, we increase the counter
        for i in range(len(nums)):
            if nums[i] != val:
                nums[counter] = nums[i]
                counter += 1
        # returns the number of items remaining
        return counter
print(Solution().removeElement([3, 2, 2, 3, 3], 3))

