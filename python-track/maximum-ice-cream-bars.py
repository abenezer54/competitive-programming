class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        minn = min(costs)
        maxx = max(costs)
        k = maxx - minn
        count = [0] * (k + 1)
        for cost in costs:
            count[cost - minn] += 1
        p = 0
        for i in range(k + 1):
            for j in range(count[i]):
                costs[p] = i + minn
                p += 1
        
        summ = 0
        for i in range(len(costs)):
            summ += costs[i]
            if summ > coins:
                return i 
                
        return len(costs)
        