class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        n, m = len(board), len(board[0])
        
        def valid(i, j): return 0 <= i < n and 0 <= j < m
        
        def count_mines(i, j):
            cnt = 0
            for x, y in directions:
                ni = x + i
                nj = y + j
                if valid(ni, nj) and board[ni][nj] == "M":
                    cnt += 1
            return cnt
        
        stack = [click]
        while stack:
            i, j = stack.pop()
            if board[i][j] == "M":
                board[i][j] = "X"
                return board
            elif board[i][j] == "E":
                cnt = count_mines(i, j)
                if cnt:
                    board[i][j] = str(cnt)
                else:
                    board[i][j] = "B"
                    for x, y in directions:
                        ni = x + i
                        nj = y + j
                        if valid(ni, nj) and board[ni][nj] == "E":
                            stack.append((ni, nj))

        return board
