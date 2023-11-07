class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        len1 = len(word1)
        len2 = len(word2)
        n = min(len1, len2)
        for i in range(n):
            ans += word1[i] + word2[i]

        if len2 > n:
            ans += word2[len1:]
        else:
            ans += word1[len2:]
            
        return ans