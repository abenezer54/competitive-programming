class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_row = Counter()
        max_col = Counter()
        for row in range(n):
            for col in range(m):
                max_row[row] = max(max_row[row], grid[row][col])
                max_col[col] = max(max_col[col], grid[row][col])

        ans = 0
        for r in range(n):
            for c in range(m):
                minn = min(max_row[r], max_col[c])
                if grid[r][c] < minn:
                    ans += minn - grid[r][c] 
                
        return ans
        