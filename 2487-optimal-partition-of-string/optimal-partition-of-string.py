class Solution:
    def partitionString(self, s: str) -> int:
        left = 0
        sett = set()
        ans = 0
        for right in range(len(s)):
            sett.add(s[right])
            if len(sett) < right - left + 1:
                ans += 1
                left = right
                sett.clear()
                sett.add(s[right])
                
        return ans + 1
        