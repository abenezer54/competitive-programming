class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        check = Counter(nums2)
        for i in range(len(nums1)):
            if check[nums1[i]] > 0:
                ans.append(nums1[i])
                check[nums1[i]] -= 1

        return ans
        