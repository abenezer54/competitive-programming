class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def dp(i):
            if memo[i] != -1:
                return memo[i]
            if i == len(nums):
                return 0
            ans = 0
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    ans = max(ans, dp(j) + 1)
            memo[i] = ans
            return memo[i]

        res = 0
        for i in range(len(nums)):
            res = max(res, dp(i))
        return res + 1
        