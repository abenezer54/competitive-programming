class Solution:
    def heightChecker(self, h: List[int]) -> int:
        c = sorted(h)
        ans = 0
        for i in range(len(h)):
            if h[i] != c[i]:
                ans += 1
        return ans
        