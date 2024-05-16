class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        for i in range(1, n):
            for j in range(m):
                minn = matrix[i - 1][j]
                if j - 1 >= 0:
                    minn = min(minn, matrix[i - 1][j - 1])
                if j + 1 < m:
                    minn = min(minn, matrix[i - 1][j + 1])
                matrix[i][j] += minn
        return min(matrix[-1])
        