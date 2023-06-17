class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                if s[l] < s[r]:
                    s = s[:r] + s[l] + s[r+1:]
                else:
                    s = s[:l] + s[r] + s[l+1:]
            l += 1
            r -= 1
        return s