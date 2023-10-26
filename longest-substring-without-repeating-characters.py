class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = left = 0
        chars = set()        
        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            ans = max(ans, right - left + 1)
        
        return ans