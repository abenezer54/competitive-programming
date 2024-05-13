class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, minn = 0, prices[0]
        for i in range(1, len(prices)):
            ans = max(ans, prices[i] - minn)
            minn = min(minn, prices[i])
        return ans
        