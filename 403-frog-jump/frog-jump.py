class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [set() for _ in range(n)]
        dp[0].add(1)
        
        for i in range(1, n):
            for j in range(i):
                distance = stones[i] - stones[j]
                if distance in dp[j]:
                    dp[i].add(distance)
                    dp[i].add(distance - 1)
                    dp[i].add(distance + 1)        
        return len(dp[-1])
        