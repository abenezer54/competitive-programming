class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        d = ((1, 0), (-1, 0), (0, 1), (0, -1))
        n, m = len(grid), len(grid[0])

        def valid(r, c):
            nonlocal n, m
            return 0 <= r < n and 0 <= c < m 

        def find_edges(i, j):
            tot = 0
            for r, c in d:
                nr = i + r
                nc = j + c
                if (valid(nr, nc) and not grid[nr][nc]) or not valid(nr, nc):
                    tot += 1
            return tot

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    ans += find_edges(i, j)
                   
        return ans
   