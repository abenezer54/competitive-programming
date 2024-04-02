class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        adj = defaultdict(set)
        n, m = len(grid), len(grid[0])
        if n == m == 1: return True
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    adj[(i, j)].add((i, j + 1))
                    adj[(i, j)].add((i, j - 1))
                elif grid[i][j] == 2:
                    adj[(i, j)].add((i + 1, j))
                    adj[(i, j)].add((i - 1, j) )
                elif grid[i][j] == 3:
                    adj[(i, j)].add((i, j - 1))
                    adj[(i, j)].add((i + 1, j) )          
                elif grid[i][j] == 4:
                    adj[(i, j)].add((i, j + 1))
                    adj[(i, j)].add((i + 1, j) )              
                elif grid[i][j] == 5:
                    adj[(i, j)].add((i, j - 1))
                    adj[(i, j)].add((i - 1, j) )
                elif grid[i][j] == 6:
                    adj[(i, j)].add((i, j + 1))
                    adj[(i, j)].add((i - 1, j))

        def valid(r, c): return 0 <= r < n and 0 <= c < m

        t = (n - 1, m - 1)
        stack = [(0, 0)]
        grid[0][0] = 0
        while stack:
            top = stack.pop()
            for r, c in adj[top]:
                if valid(r, c) and grid[r][c] and (top[0], top[1]) in adj[(r, c)]:
                    grid[r][c] = 0
                    if (r, c) == t:
                        return True
                    stack.append((r, c))
        return False
