class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        summ = 0
        for r in range(n):
            for c in range(n):
                if not r - c:
                    summ += mat[r][c]
                if r + c  == n - 1:
                    summ += mat[r][c]
        if n & 1:
            summ -= mat[n // 2][n // 2]
        
        return summ
        