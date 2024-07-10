class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n - 3 < 2:
            return 0
        ans = float('inf')
        for i in range(4):
            ans = min(ans, nums[i + n - 3 - 1] - nums[i])
        return ans
        