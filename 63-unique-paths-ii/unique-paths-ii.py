class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        def inbound(i, j): return 0 <= i < n and 0 <= j < m

        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1 if not grid[0][0] else 0
        # print(dp)
        for i in range(n):
            for j in range(m):
                if not grid[i][j]:
                    if inbound(i - 1, j) and not grid[i - 1][j]:
                        dp[i][j] += dp[i - 1][j]
                    if inbound(i, j - 1) and not grid[i][j - 1]:
                        dp[i][j] += dp[i][j - 1]
        return dp[-1][-1]
        