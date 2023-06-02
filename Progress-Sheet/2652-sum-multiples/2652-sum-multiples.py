class Solution:
    def sumOfMultiples(self, n: int) -> int:
        ans = 0
        for i in range(3, n+1):
            if i %3 == 0: 
                ans += i
            elif  i % 5== 0:
                ans += i
            elif i % 7 == 0:
                ans += i
        return ans