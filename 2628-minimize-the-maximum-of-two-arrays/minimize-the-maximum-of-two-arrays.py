class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        l, r = 1, (1 << 32) - 1
        lcmm = lcm(divisor1, divisor2)
        while l + 1 < r:
            mid = (l + r) // 2
            if mid - (mid // divisor1) >= uniqueCnt1 and mid - (mid // divisor2) >= uniqueCnt2 and mid - (mid // lcmm) >= uniqueCnt1 + uniqueCnt2:
                r = mid
            else:
                l = mid
        return r 
        