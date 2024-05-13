class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [(-prices[0], 0), (-prices[0], 0)]
        for i in range(len(prices)):
            val1 = max(dp[-1][0], dp[-2][1] - prices[i])
            val2 = max(dp[-1][1], dp[-1][0] + prices[i])
            dp.append((val1, val2))
        return max(dp[-1])
        