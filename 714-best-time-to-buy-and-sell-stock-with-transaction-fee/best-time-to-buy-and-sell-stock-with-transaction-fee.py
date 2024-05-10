class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [(0, -prices[0])]
        for i in range(1, len(prices)):
            dp.append((max(dp[-1][0], dp[-1][1] + prices[i] - fee),max(dp[-1][1], dp[-1][0] - prices[i])))
        return max(dp[-1][0], dp[-1][1])