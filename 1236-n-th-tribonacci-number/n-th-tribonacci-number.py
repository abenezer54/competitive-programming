class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            if n == 2: return 1
            return n
            
        a, b, c = 0, 1, 1
        for i in range(3, n + 1):
            x = a + b + c
            a, b, c = b, c, x

        return c
        