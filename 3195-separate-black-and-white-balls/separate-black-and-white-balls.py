class Solution:
    def minimumSteps(self, s: str) -> int:
        l = 0
        n = len(s)
        ans = 0
        for r in range(n):
            if s[r] == "0":
                ans += r - l
                l += 1
        return ans
        