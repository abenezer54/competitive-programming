class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        a, b = 0, 1
        for i in range(n):
            temp = a + b
            a = b
            b = temp
        return b