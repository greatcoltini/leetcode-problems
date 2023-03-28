class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        combined = []

        for elem in nums1:
            if elem in nums2 and elem not in combined:
                combined.append(elem)
        
        return combined
