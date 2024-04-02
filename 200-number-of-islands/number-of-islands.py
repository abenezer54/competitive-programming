class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        d = ((1, 0), (-1, 0), (0, 1), (0, -1))
        def valid(i, j): return 0 <= i < n and 0 <= j < m and grid[i][j] == '1'

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    stack = [(i, j)]
                    ans += 1
                    while stack:
                        top = stack.pop()
                        for r, c in d:
                            ni = r + top[0]
                            nj = c + top[1]
                            if valid(ni, nj):
                                grid[ni][nj] = 0
                                stack.append((ni, nj))
        return ans
        