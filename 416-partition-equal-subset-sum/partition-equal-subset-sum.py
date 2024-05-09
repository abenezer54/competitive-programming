class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot & 1: return False
        half = tot // 2
        
        dp = [0] * (half + 1)
        for num in nums:
            for i in range(half, -1, -1):
                if dp[i] and (i + num) <= half:
                    dp[i + num] = 1
            if num <= half:
                dp[num] = 1

        return dp[half]
