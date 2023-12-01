class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        minn = min(len(word1), len(word2))
        for i in range(minn):
            ans += word1[i] + word2[i]
        ans += word1[minn:] + word2[minn:]
        
        return ans
