class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        else:
            maxx = 0
            l = 0
            r = 1
            while l < r and r < len(prices):
                print(prices[l], prices[r])
                if prices[r] <= prices[l]:
                    l = r
                    r += 1
                else:
                    diff = prices[r] - prices[l]
                    if diff > maxx:
                        maxx = diff
                    r += 1
            return maxx
                    