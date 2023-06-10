class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        print(prices)
        i = 0
        while i < len(prices):
            if (prices[i] + prices[i + 1]) > money:
                return money
            else:
                return money - (prices[i] + prices[i + 1])