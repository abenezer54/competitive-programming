class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        nxt, n = {}, len(arr)
        dp = [1] * n

        for i in range(n - 1, -1, -1):
            if arr[i] + diff in nxt:
                dp[i] += dp[nxt[arr[i] + diff]]
            nxt[arr[i]] = i

        return max(dp)
        