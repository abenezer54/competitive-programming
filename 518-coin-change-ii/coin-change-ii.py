class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1) 
        dp[0] = 1
        for coin in coins:
            if coin <= amount:
                for j in range(amount + 1):
                    if j + coin <= amount:
                        dp[j + coin] += dp[j]
        return dp[-1]
        