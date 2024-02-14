class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        for r in range(n):
            for c in range(1, m):
                matrix[r][c] += matrix[r][c - 1]
        
        ans = 0
        for left in range(m):
            for right in range(left, m):
                count = Counter()
                count[0] = 1
                summ = 0

                for row in range(n):
                    summ += matrix[row][right] - (matrix[row][left - 1] if left > 0 else 0)
                    ans += count[summ - target]
                    count[summ] += 1

        return ans
