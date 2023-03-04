class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # each item appears twice, so we create array and pop all repeat offenders
        singular = []

        for num in nums:
            if num not in singular:
                singular.append(num)
            else:
                singular.remove(num)
        
        return singular[0]
        