class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)//3
        print(n)
        piles.sort()
        count = 0
        for i in range(n, len(piles), 2):
            count += piles[i]
        return count
        