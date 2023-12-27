class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0 for col in range(n)] for row in range(m)]

        for row, col in guards:
            grid[row][col] = "G"

        for row, col in walls:
            grid[row][col] = "W"
        
        for row, col in guards:
            r1 = row - 1
            while r1 >= 0 and grid[r1][col] not in ["W", "G"]:
                grid[r1][col] = 1
                r1 -= 1

            r2 = row + 1
            while r2 < m and grid[r2][col] not in ["W", "G"]:
                grid[r2][col] = 1
                r2 += 1

            c1 = col - 1
            while c1 >= 0 and grid[row][c1] not in ["W", "G"]:
                grid[row][c1] = 1
                c1 -= 1

            c2 = col + 1
            while c2 < n and grid[row][c2] not in ["W", "G"]:
                grid[row][c2] = 1
                c2 += 1

        ans = 0
        for r in range(m):
            for c in range(n):
                if not grid[r][c]:
                    ans += 1

        return ans
        