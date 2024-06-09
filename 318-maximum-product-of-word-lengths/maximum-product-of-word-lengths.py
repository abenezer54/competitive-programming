class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        cnt = [0] * n
        for i, word in enumerate(words):
            for ch in word:
                bit = ord(ch) - 97
                cnt[i] |= 1 << bit
        
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                for bit in range(26):
                    if  (cnt[i] & (1 << bit)) and cnt[j] & (1 << bit):
                        break
                else:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans        
        