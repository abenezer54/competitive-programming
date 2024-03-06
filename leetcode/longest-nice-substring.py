class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ''
        def longest(l, r):
            nonlocal ans
            count = set()
            for i in range(l, r):
                count.add(s[i])
            
            for i in range(l, r):
                if s[i].swapcase() not in count:
                    idx = i
                    break
            else:
                if r - l > len(ans):
                    ans = s[l: r]
                return
            longest(l, idx)
            longest(idx + 1, r)
        longest(0, len(s))
        return ans
        