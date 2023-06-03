class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort() 
        if coins < costs[0]:
            return 0
        iceCream = 0
        summ = 0
        for c in costs:
            summ += c
            if summ <= coins:
                iceCream += 1
        return iceCream