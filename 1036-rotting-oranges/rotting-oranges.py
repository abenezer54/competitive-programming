class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n, m = len(grid), len(grid[-1])
        def valid(i, j): return 0 <= i < n and 0 <= j < m and grid[i][j] == 1 
        fresh = 0
        que = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    que.append((i, j))
        minute = 0
        while que:
            if fresh == 0: return minute
            l = len(que)
            for _ in range(l):
                i, j = que.popleft()
                for r, c in d:
                    ni, nj = i + r, j + c
                    if valid(ni, nj):
                        que.append((ni, nj))
                        fresh -= 1
                        grid[ni][nj] = 2
            minute += 1
        return -1 if fresh else 0

        