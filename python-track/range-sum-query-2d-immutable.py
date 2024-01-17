class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.p = [[0] * (m + 1) for _ in range(n + 1)]
        for r in range(n):
            for c in range(m):
                self.p[r + 1][c + 1] = self.p[r][c + 1] + self.p[r + 1][c] - self.p[r][c] + matrix[r][c]
        

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        ans = self.p[r2 + 1][c2 + 1] - self.p[r2 + 1][c1] - self.p[r1][c2 + 1] + self.p[r1][c1]
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)