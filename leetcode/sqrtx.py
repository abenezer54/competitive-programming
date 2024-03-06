class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x + 1
        while l + 1 < r:
            mid = (l + r) // 2
            if mid * mid <= x:
                l = mid    
            else:
                r = mid
        return l
        