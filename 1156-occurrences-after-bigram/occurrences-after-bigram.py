class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        t = text.split()
        n = len(t)
        ans = []
        for i in range(2, n):
            if t[i - 1] == second and t[i - 2] == first:
                ans.append(t[i])
        return ans
        