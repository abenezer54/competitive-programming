class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        def inbound(i, j): return 0 <= i < n and 0 <= j < m
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        vis = set()
        que = deque()
        for i in range(n):
            for j in range(m):
                if not mat[i][j]:
                    que.append((i, j))
                    vis.add((i, j))

        ans = [[0] * m for _ in range(n)]
        move = 0
        while que:
            l = len(que)
            for _ in range(l):
                i, j = que.popleft()
                ans[i][j] = move
                for r, c in d:
                    ni, nj = r + i, c + j 
                    if inbound(ni, nj) and (ni, nj) not in vis:
                        que.append((ni, nj))
                        vis.add((ni, nj))
            move += 1 
        return ans       