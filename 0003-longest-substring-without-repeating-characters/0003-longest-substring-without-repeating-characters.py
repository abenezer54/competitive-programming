class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        dic = {}
        l = 0
        maxx = 0
        for r in range(len(s)):
            if s[r] in dic and dic[s[r]] >= l:
                l = dic[s[r]] + 1
            dic[s[r]] = r
            maxx = max(maxx, r - l + 1)
        return maxx