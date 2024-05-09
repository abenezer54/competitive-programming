class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) > 2:
            nums[2] += nums[0]
        for i in range(3, n):
            nums[i] += max(nums[i - 2], nums[i - 3])
        
        return max(nums)
        