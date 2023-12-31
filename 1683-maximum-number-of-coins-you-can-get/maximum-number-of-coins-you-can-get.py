class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        bob = len(piles) // 3
        
        ans = 0
        for i in range(1, len(piles) - bob + 1, 2):
            ans += piles[i]

        return ans
