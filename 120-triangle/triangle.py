class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                x = triangle[i - 1][j - 1] if j - 1 >= 0 else float('inf')
                y = triangle[i - 1][j] if j < len(triangle[i - 1]) else float('inf')
                triangle[i][j] += min(x, y)
        return min(triangle[-1])
        