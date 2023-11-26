class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        cur = 0
        for i in range(len(s)):
            if s[i] == "0":
                ans += i - cur
                cur += 1

        return ans
        