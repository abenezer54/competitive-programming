class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = list(set(nums1))
        n2 = list(set(nums2))
        ans = []
        for i in range(len(n1)):
            if n1[i] in n2:
                ans.append(n1[i])
        return ans