class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0
        for i in range(1, n + 1):
            if i % m:
                num1 += i
            else:
                num2 += i
    
        return num1 - num2
        