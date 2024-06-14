class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        mx, ans = nums[0], 0
        
        for i in range(1, len(nums)):
            if nums[i] <= mx:
                ans += mx + 1 - nums[i]
                mx += 1
            mx = max(mx, nums[i])
        return ans
        