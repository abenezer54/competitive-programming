class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        l = 0
        r = 1
        ans = prices
        while l < len(prices) and r < len(prices):
            # print(ans)
            # print(l, r)
            if prices[r] <= prices[l]:
                ans[l] = prices[l] - prices[r]
                l += 1
                r = l + 1
            else:
                if r == (len(prices) - 1):
                    l += 1
                    r = l + 1
                else:
                    r += 1
        return ans