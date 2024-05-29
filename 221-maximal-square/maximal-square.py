class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        ans = 1 if '1' in matrix[0] else 0
        for i in range(1, n):
            ans = max(ans, int(matrix[i][0]))
            for j in range(1, m):
                if matrix[i][j] =='1':
                    minn = min(int(matrix[i - 1][j - 1]), int(matrix[i][j - 1]), int(matrix[i - 1][j]))
                    matrix[i][j] = int(matrix[i][j]) + minn
                ans = max(ans, int(matrix[i][j]))
        return ans * ans
        