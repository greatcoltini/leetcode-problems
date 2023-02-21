class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        compare = nums[0]
        uniques = 1
        write_index = 1
        repeats = 0

        for item in nums[1:]:
            if item != compare:
                uniques += 1
                compare = item
                nums[write_index] = item
                write_index += 1
            else:
                repeats += 1

        return uniques
        



            