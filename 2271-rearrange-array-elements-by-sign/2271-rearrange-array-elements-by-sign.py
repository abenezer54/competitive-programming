class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        p1 = 0
        p2 = 1
        for i in range(len(nums)):
            if nums[i] > 0:
                ans[p1] = nums[i]
                p1 += 2
            elif nums[i] < 0:
                ans[p2] = nums[i]
                p2 += 2
        return ans
            
