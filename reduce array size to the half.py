from collections import Counter


class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # create initial variables
        set_size = 0
        items = 0

        # we create a key - value dictionary of count of items in array
        values = reversed(sorted(Counter(arr).values()))
        length = len(arr)

        # we enumerate through this array, until we hit half of size
        for count, value in enumerate(values):
            if set_size < length // 2:
                set_size += value
                items += 1
            else:
                return items
        return items