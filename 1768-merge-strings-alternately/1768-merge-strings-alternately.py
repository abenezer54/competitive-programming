class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        maxx = max(len(word1), len(word2))
        ans = ""
        for i in range(maxx):
            if i < len(word1):
                ans += word1[i]
            if i < len(word2):
                ans += word2[i]
        return ans