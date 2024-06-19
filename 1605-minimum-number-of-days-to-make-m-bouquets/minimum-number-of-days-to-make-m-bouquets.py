class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k > n:
            return -1
        
        def canMakeBouquets(d):
            bouquets = 0
            flowers = 0
            for bloom in bloomDay:
                if bloom <= d:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1 
                        flowers = 0
                else:
                    flowers = 0
            return bouquets >= m
        
        left , right = min(bloomDay), max(bloomDay)

        while left < right:
            mid = (left + right) // 2
            if canMakeBouquets(mid):
                right = mid
            else:
                left = mid + 1
        return left
        