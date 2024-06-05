class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ans = 0
        memo = {}
        def dp(num, depth):
            if num == target:
                return 1
            if (num, depth) in memo:
                return memo[(num, depth)]
            cur = 0
            for i in nums:
                if num + i <= target:
                    cur += dp(num + i, depth + 1)
            memo[(num, depth)] = cur
            return cur
        return dp(0, 0)
        