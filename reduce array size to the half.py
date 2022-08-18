class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        # initialization of the required variables
        integer_occurrences = {}
        array_len = len(arr)
        removed_num = 0
        min_set = 0

        # loop through array, create dict storing occurrences
        for item in arr:
            if item in integer_occurrences:
                integer_occurrences[item] += 1
            else:
                integer_occurrences[item] = 1

        # while our removed integers value is less than half the array, we continue to parse dict
        while removed_num <= (array_len / 2):
            highest_occ_int = max(integer_occurrences, key=integer_occurrences.get)
            removed_num = removed_num + max(integer_occurrences, key=integer_occurrences.get)
            del integer_occurrences[highest_occ_int]
            min_set += 1

        # return the minimum number of integers to be removed to make the array <= half of its initial size
        return min_set

print(Solution().minSetSize([3, 3]))

print(Solution().minSetSize([3, 3, 4, 4]))

Solution().minSetSize([3, 3, 5, 6])

Solution().minSetSize([3, 3, 7, 8, 9, 10])

print(Solution().minSetSize([1, 2, 3, 4, 5, 6]))
