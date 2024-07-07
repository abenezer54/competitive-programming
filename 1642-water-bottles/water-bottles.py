class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = r = numBottles
        while r >= numExchange:
            ans += r // numExchange
            r = (r // numExchange) + (r % numExchange)
        return ans
        