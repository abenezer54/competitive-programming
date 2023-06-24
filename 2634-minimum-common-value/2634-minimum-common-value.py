class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        p1 = 0
        p2 = 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                return nums1[p1]
            else:
                if nums1[p1] < nums2[p2]:
                    p1 += 1
                else:
                    p2 += 1
        return -1