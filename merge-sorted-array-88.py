class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # traverse lists backwards
        counter = m + n
        index_1 = m - 1
        index_2 = n - 1
        if m > 0 and n > 0:
            while counter >= 1:
                if index_1 >= 0 and index_2 >= 0:
                    if nums1[index_1] < nums2[index_2]:
                        nums1[counter - 1] = nums2[index_2]
                        index_2 = index_2 - 1
                    elif nums1[index_1] > nums2[index_2]:
                        nums1[counter - 1] = nums1[index_1]
                        index_1 = index_1 - 1
                    else:
                        nums1[counter - 1] = nums1[index_1]
                        index_1 = index_1 - 1
                elif index_1 < 0 and index_2 >= 0:
                    nums1[counter - 1] = nums2[index_2]
                    index_2 = index_2 - 1
                elif index_1 >= 0 and index_2 < 0:
                    nums1[counter - 1] = nums1[index_1]
                    index_1 = index_1 - 1
                counter = counter - 1
        elif n > 0 and m == 0:
            while counter > 0:
                nums1[counter - 1] = nums2[counter - 1]
                counter = counter - 1

          
                    
                        