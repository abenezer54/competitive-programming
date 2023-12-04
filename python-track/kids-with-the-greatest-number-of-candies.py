class Solution:
    def kidsWithCandies(self, candies: List[int], extra: int) -> List[bool]:
        return [c + extra >= max(candies) for c in candies]
        