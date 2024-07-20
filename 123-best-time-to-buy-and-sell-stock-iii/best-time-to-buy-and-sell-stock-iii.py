class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = buy2 = float("inf")
        sell1 = sell2 = 0
        
        for cur in prices:
            buy1 = min(buy1, cur)
            sell1 = max(sell1, cur - buy1)

            buy2 = min(buy2, cur - sell1)
            sell2 = max(sell2, cur - buy2)
        return sell2
        