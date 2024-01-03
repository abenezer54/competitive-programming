class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        p = 0
        for i in range(len(s)):
            if p < len(g) and s[i] >= g[p]:
                p += 1
                
        return p
