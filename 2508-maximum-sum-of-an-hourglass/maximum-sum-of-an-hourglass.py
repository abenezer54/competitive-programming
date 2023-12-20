class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        answer = 0
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                current = grid[i][j]
                current += grid[i - 1][j] + grid[i + 1][j] 
                current += grid[i - 1][j - 1] + grid[i - 1][j + 1]
                current += grid[i + 1][j - 1] + grid[i + 1][j + 1]
                answer = max(answer, current)
        return answer
        