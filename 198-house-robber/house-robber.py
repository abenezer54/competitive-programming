class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n > 2: nums[2] += nums[0]
        for i in range(3, n):
            nums[i] += max(nums[i - 2], nums[i - 3])      
        return max(nums[-1], nums[-2]) if n >  1 else nums[0]
        