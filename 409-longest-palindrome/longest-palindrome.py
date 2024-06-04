class Solution:
    def longestPalindrome(self, s: str) -> int:
        hv = False
        cnt = Counter(s)
        ans = 0
        for k, v in cnt.items():
            if v & 1:
                hv = True
                ans += v - 1
            else:
                ans += v
        return ans + 1 if hv else ans
        