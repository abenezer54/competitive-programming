class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        odd = ans = 0
        for value in c.values():
            if value & 1:
                odd += 1
                ans += value - 1
            else:
                ans += value
        if odd:
            ans += 1
            
        return ans
        