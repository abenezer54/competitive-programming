class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        sums = sorted([weights[i] + weights[i + 1] for i in range(len(weights) - 1)])
        return sum(sums[-k + 1:]) - sum(sums[:k - 1])

      
