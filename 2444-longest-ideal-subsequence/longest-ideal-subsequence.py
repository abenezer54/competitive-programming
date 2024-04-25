class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for char in s:
            i = ord(char) - 97
            mx = max(dp[max(0, i - k): min(25, i + k) + 1])
            dp[i] = mx + 1
        return max(dp)              
        