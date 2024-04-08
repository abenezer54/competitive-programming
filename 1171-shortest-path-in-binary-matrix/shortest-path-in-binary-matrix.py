class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]: return -1
        d = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]
        n = len(grid)
        def valid(i, j): return 0 <= i < n and 0 <= j < n and not grid[i][j]

        que = deque([(0, 0)])
        length = 1
        while que:
            l = len(que)

            for _ in range(l):
                i, j = que.popleft()
                if i == j == n - 1: return length
                for r, c in d:
                    ni, nj = r + i, c + j
                    if valid(ni, nj):
                        que.append((ni, nj))
                        grid[ni][nj] = 2

            length += 1
        
        return -1
