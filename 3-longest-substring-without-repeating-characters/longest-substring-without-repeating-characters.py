class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        check = set()
        ans = 0
        for r in range(n): 
            while s[r] in check:
                check.discard(s[l])
                l += 1
            check.add(s[r])
            ans = max(ans, len(check))
        return ans
       