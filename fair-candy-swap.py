class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes) - sum(bobSizes)) / 2
        aliceSizes = set(aliceSizes)
        for candy in set(bobSizes):
            if diff + candy in aliceSizes:
                return [diff + candy, candy]