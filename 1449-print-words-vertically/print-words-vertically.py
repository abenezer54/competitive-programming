class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        maxx = max([len(word) for word in s])
        ans = [""] * maxx
        for i in range(len(s)):
            if len(s[i]) < maxx:
                s[i] += " " * (maxx - len(s[i]))
        for i in range(len(s)):
            for j in range(len(s[i])):
                ans[j] += s[i][j]
        for i in range(maxx):
            ans[i] = ans[i].rstrip()

        return ans
        