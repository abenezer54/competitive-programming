class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(i, j): return 0 <= i < n and 0 <= j < m
        def checkwayout(i, j):
            for r, c in d:
                ni, nj = i + r, j + c
                if not inbound(ni, nj):
                    return True
            return False
        vis = set()
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and (i, j) not in vis:
                    stack = [(i, j)]
                    cur = [(i, j)]
                    vis.add((i, j ))
                    wayout = checkwayout(i, j)
                    while stack:
                        r, c = stack.pop()
                        for x, y in d:
                            ni, nj = x + r, y + c
                            if inbound(ni, nj) and board[ni][nj] == "O" and (ni, nj) not in vis:
                                vis.add((ni, nj))
                                stack.append((ni, nj))
                                cur.append((ni, nj))
                                if checkwayout(ni, nj):
                                    wayout = True
                    if not wayout:
                        while cur:
                            r, c = cur.pop()
                            board[r][c] = "X"
        return board


        
        