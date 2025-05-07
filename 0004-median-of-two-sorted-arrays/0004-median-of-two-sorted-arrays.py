class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_lst = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                new_lst.append(nums1[i])
                i += 1
            else:
                new_lst.append(nums2[j])
                j += 1

        while i < len(nums1):
            new_lst.append(nums1[i])
            i += 1
        while j < len(nums2):
            new_lst.append(nums2[j])
            j += 1

        n = len(new_lst)
        if n % 2 == 0:
            return (new_lst[n // 2 - 1] + new_lst[n // 2]) / 2.0
        else:
            return new_lst[n // 2]
