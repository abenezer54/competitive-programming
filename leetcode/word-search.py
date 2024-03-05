class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        cur = []
        visited = set()

        def is_valid(pair):
            row, col = pair
            if row < n and row >= 0 and col >= 0 and col < m:
                return True

        def backtrack(pair, index):     
            row, col = pair
            if index == len(word) - 1:
                return True
            

            candidates = [(row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)]
            for candidate in candidates:
                r, c = candidate
                visited.add(pair)
                if is_valid(candidate) and word[index + 1] == board[r][c] and candidate not in visited:
                    if backtrack(candidate, index + 1):
                        return True
                visited.discard(pair)
            

        ans = False
        for row in range(n):
            for col in range(m):
                if word[0] == board[row][col]:
                    if backtrack((row, col), 0):
                        return True
