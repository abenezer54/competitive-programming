class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def isNice(a):
            arr = [x for x in a]
            ans = all(x.swapcase() in arr for x in arr)
            return ans

        ans = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                word = s[i:j+1]
                if isNice(word) and len(ans) < (j - i + 1):
                    ans = word
        
        return ans