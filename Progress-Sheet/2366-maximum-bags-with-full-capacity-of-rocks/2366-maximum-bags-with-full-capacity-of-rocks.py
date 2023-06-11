class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remaining = [0] * len(capacity)
        for i in range(len(capacity)):
            remaining[i] = capacity[i] - rocks[i]
        remaining.sort()
        print(remaining)
        summ = 0
        i = 0
        while i < len(remaining) and summ + remaining[i] <= additionalRocks:
            summ += remaining[i]
            i += 1
        return i