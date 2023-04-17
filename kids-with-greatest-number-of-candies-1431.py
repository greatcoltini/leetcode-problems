class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        # get minimum value to have greatest number of candies
        minimum_val = max(candies)

        true_kids = []

        # sort array
        for kid in candies:
            current_candy = kid + extraCandies
            if current_candy >= minimum_val:
                true_kids.append(True)
            else:
                true_kids.append(False)
        
        return true_kids