class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}
        def dp(t):
            if t == 1 or t == 0:
                return 1
            if t in memo:
                return memo[t]
            ans = t if t != n else 1
            for i in range(1, (t // 2) + 1):
                ans = max(ans, dp(i) * dp(t - i))
            memo[t] = ans
            return memo[t]
        return dp(n)
        