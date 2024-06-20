class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        def check(d):
            cnt, prev = 1, 0
            for i in range(1, n):
                if position[i] - position[prev] >= d:
                    cnt += 1
                    prev = i
            return cnt >= m
            
        l, r = 0, position[-1] - position[0] + 1
        while l + 1 < r:
            mid = (l + r) // 2
            if check(mid):
                l = mid
            else:
                r = mid
        return l
        