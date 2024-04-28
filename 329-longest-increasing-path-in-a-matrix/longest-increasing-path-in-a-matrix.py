class Solution:
    def longestIncreasingPath(self, mat: List[List[int]]) -> int:
        adj = defaultdict(set)
        ind = defaultdict(int)
        n, m = len(mat), len(mat[0])
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(i, j): return 0 <= i < n and 0 <= j < m

        for i in range(n):
            for j in range(m):
                for r, c in d:
                    ni, nj = r + i, c + j
                    if inbound(ni, nj):
                        if mat[ni][nj] > mat[i][j]:
                            if (ni, nj) not in adj[(i, j)]:
                                adj[(i, j)].add((ni, nj))
                                ind[(ni, nj)] += 1
                        elif mat[ni][nj] < mat[i][j]:
                            if (i, j) not in adj[(ni, nj)]:
                                adj[(ni, nj)].add((i, j))
                                ind[(i, j)] += 1
        que = deque()
        for i in range(n):
            for j in range(m):
                if not (i, j) in ind:
                    que.append((i, j))

        move = 0
        while que:
            l = len(que)
            for _ in range(l):
                i, j = que.popleft()
                for ni, nj in adj[(i, j)]:
                    ind[(ni, nj)] -= 1
                    if not ind[(ni, nj)]:
                        que.append((ni, nj))
            move += 1
        return move
