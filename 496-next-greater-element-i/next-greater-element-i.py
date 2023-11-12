class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num in nums1:
            idx = nums2.index(num)
            print(idx)
            found = False
            for i in range(idx, len(nums2)):
                if nums2[i] > num:
                    ans.append(nums2[i])
                    found = True
                    break
            if not found:
                ans.append(-1)
        return ans
        