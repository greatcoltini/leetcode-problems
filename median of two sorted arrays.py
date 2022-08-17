class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_arr = self.mergeArrays(nums1, nums2)
        return self.findMedian(merged_arr)

    def mergeArrays(self, arr1, arr2):
        """
        Merge two sorted arrays, also in sorted order
        :param arr1:
        :param arr2:
        :return:
        """
        merged_arr = []

        while arr1:
            if arr2:
                if arr1[0] < arr2[0]:
                    merged_arr.append(arr1.pop(0))
                elif arr1[0] == arr2[0]:
                    merged_arr.append(arr1.pop(0))
                    merged_arr.append(arr2.pop(0))
                else:
                    merged_arr.append(arr2.pop(0))
            else:
                merged_arr.append(arr1.pop(0))
        while arr2:
            merged_arr.append(arr2.pop(0))
        return merged_arr

    def findMedian(self, arr):
        if len(arr) % 2 == 1:
            middle_val = arr[len(arr) // 2]
            return arr[middle_val]
        else:
            middle_vals = [arr[len(arr) // 2 - 1], arr[len(arr) // 2]]
            print(middle_vals)
            median = (middle_vals[0] + middle_vals[1]) / 2
            return median
