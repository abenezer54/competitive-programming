class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        ans = 0
        if abs(fx - sx) == 0 and abs(fy - sy) == 0:
            print("fir")
            if t > 0:
                ans = 2
        elif abs(fx - sx) < abs(fy - sy):
            ans += abs(fx - sx) + (abs(fy - sy) - abs(fx - sx))
        elif abs(fx - sx) > abs(fy - sy):
            ans += abs(fy - sy) + (abs(fx - sx) - abs(fy - sy))
        else:
            ans += abs(fy - sy)
        print(ans)
        return ans <= t
