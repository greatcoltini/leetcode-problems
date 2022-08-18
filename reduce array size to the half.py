class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        integer_occurences = {}
        array_len = len(arr)
        removed_num = 0
        min_set = 0

        # loop through array, create dict storing occurences
        for item in arr:
            if item in integer_occurences:
                integer_occurences[item] += 1
            else:
                integer_occurences[item] = 1

        while removed_num <= (array_len // 2):
            highest_occ_int = max(integer_occurences, key=integer_occurences.get)
            removed_num = removed_num + max(integer_occurences, key=integer_occurences.get)
            del integer_occurences[highest_occ_int]
            min_set += 1
            print(removed_num)

        print(integer_occurences)
        print(min_set)

Solution().minSetSize([3, 3])