class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0: return 1
        if n == 1: return x
        if n == 2: return x * x
        

        if n < 0: return 1 / self.myPow(x, abs(n))

        if n & 1: return self.myPow(self.myPow(x, n // 2), 2) * x

        if not n & 1: return self.myPow(self.myPow(x, n // 2), 2)
        