class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # parse list until we get expected area (log previous int and current int, if our target is between two we insert before)
        length = len(nums)
        previous, current = nums[0], nums[1]
        for num in nums[2:]:
            if previous == target:
                return nums.index(previous)
            elif current == target:
                return nums.index(current)
            elif previous > target:
                if nums.index(previous) == 0:
                    return 0
                else:
                    return nums.index(previous) - 1
            elif current < target and index(current) == length:
                return nums.index(current) + 1
            elif current > target and target > previous:
                return nums.index(previous)
            
            previous = current
            current = num
        return 1

