class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        row = [float('inf')] * n
        col = [0] * m
        for i in range(n):
            for j in range(m):
                row[i] = min(row[i], matrix[i][j])
                col[j] = max(col[j], matrix[i][j])

        ans = []
        for i in range(n):
            for j in range(m):
                if row[i] == matrix[i][j] and col[j] == matrix[i][j]:
                    ans.append(matrix[i][j])
        
        return ans
        