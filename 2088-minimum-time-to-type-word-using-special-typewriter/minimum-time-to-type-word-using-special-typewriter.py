class Solution:
    def minTimeToType(self, word: str) -> int:
        ans = 0
        cur = 97
        for char in word:
            diff = min(abs(ord(char) - cur), cur -(ord(char) - 26),abs(cur -(ord(char) + 26))) 
            ans += diff + 1
            cur = ord(char)
            
        return ans
        