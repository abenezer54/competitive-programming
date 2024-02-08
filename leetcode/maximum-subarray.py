class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = -float("inf")
        minn = cur = 0 
        n = len(nums)
        for i in range(n):
            cur += nums[i]
            maxx = max(maxx, cur - minn)
            minn = min(minn, cur)
        return maxx
        