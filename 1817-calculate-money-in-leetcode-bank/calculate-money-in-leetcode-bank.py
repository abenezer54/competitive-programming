class Solution:
    def totalMoney(self, n: int) -> int:
        current = 1
        i = 1
        ans = 0
        while i <= n:
            ans += current
            current += 1
            if i % 7 == 0:
                current = (i // 7) + 1
            i += 1
        
        return ans
  