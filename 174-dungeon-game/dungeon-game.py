class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if i == n - 1 and j == m - 1:
                    if dungeon[i][j] > 0:
                        dungeon[i][j] = 0
                    continue
                choice1 = dungeon[i + 1][j] if i + 1 < n else -float('inf')
                choice2 = dungeon[i][j + 1] if j + 1 < m else -float('inf')
                dungeon[i][j] += max(choice1, choice2)
                if dungeon[i][j] > 0:
                    dungeon[i][j] = 0
                    
        return abs(dungeon[0][0]) + 1 if dungeon[0][0] < 0 else 1
        