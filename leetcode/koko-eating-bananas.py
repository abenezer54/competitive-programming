class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculate_hour(speed):
            hour = 0
            for i in range(len(piles)):
                hour += ceil(piles[i] /  speed)
            return hour
        l, r = 0, max(piles)
        while l + 1 < r:
            mid = (l + r) // 2
            if calculate_hour(mid) <= h:
                r = mid
            else:
                l = mid
        return r