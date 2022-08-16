class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numMap = {}
        counter = 0
        # add each item to dict
        for item in nums:
            # remainder is what we are searching for as another element of the list
            remainder = target - item

            # we check if the remainder exists in the hashmap
            # ensure that it is not the item we are currently viewing
            if remainder in numMap and numMap[remainder] != counter:
                return [numMap[remainder], counter]
            # we add every item in nums to this hashmap
            numMap[item] = counter
            counter += 1

        return
