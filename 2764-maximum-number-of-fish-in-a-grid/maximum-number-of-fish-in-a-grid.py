class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        p = list(range(n * m))
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def inbound(i, j): return 0 <= i < n and 0 <= j < m
        def convert(i, j): return (m * i) + j
        size = [0] * (n * m)
        for r in range(n):
            for c in range(m):
                if grid[r][c]:
                    size[convert(r, c)] = grid[r][c]
        def find(a):
            rt = a
            while rt != p[rt]:
                rt = p[rt]

            while a != rt:
                nxt = p[a]
                p[a] = rt
                a = nxt
            return rt
    
        def union(a, b):
            rta, rtb = find(a), find(b)
            if rta != rtb:
                if size[rtb] > size[rta]:
                    p[rta] = rtb
                    size[rtb] += size[rta]
                else:
                    p[rtb] = rta
                    size[rta] += size[rtb]

        for r in range(n):
            for c in range(m):
                if grid[r][c]:
                    for i, j in d:
                        nr, nc = i + r, j + c
                        if inbound(nr, nc) and grid[nr][nc]:
                            union(convert(nr, nc), convert(r, c))
                            
        return max(size)      
        