class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        for bit in range(32):
            v = 1 << bit
            ln = v - (left % v)
            if left + ln <= right:
                left &= (~v)
        return left
    