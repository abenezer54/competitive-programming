class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        N = len(rocks)
        free = [0] * N
        for i in range(N):
            free[i] = capacity[i] - rocks[i]
        free.sort()
        ans = 0
        summ = 0
        for j in range(N):
            summ += free[j]
            if summ <= additionalRocks:
                ans += 1
        return ans
        