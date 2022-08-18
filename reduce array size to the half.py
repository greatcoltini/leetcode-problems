class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        # initialization of the required variables
        integer_occurrences = {}
        removed_num_integers = 0
        min_set = 0

        # sort array first
        sorted_arr = reversed(sorted(arr))
        for count, value in enumerate(sorted_arr):
            if value in integer_occurrences:
                integer_occurrences[value] += 1
            else:
                integer_occurrences[value] = 1
            count += 1

        # while our removed integers value is less than half the array, we continue to parse dict
        while removed_num_integers < (count // 2):
            highest_occ_int = max(integer_occurrences, key=integer_occurrences.get)
            removed_num_integers = removed_num_integers + integer_occurrences[highest_occ_int]
            del integer_occurrences[highest_occ_int]
            min_set += 1

        # return the minimum number of integers to be removed to make the array <= half of its initial size
        return min_set

print(Solution().minSetSize([3, 3]))

print(Solution().minSetSize([3, 3, 4, 4]))

#Solution().minSetSize([3, 3, 5, 6])

print(Solution().minSetSize([3,3,3,3,5,5,5,2,2,7]))

print(Solution().minSetSize([10, 10, 9, 1]))


#def minSetSize(self, arr: List[int]) -> int:
#    return next(i+1 for i,n in enumerate(accumulate(reversed(sorted(Counter(arr).values())))) if n >= len(arr)//2)
