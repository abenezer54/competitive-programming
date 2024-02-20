class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last, n  = Counter(), len(s)
        for i in range(n):
            last[s[i]] = i

        l, end, ans = 0, 0, []
        for i in range(n):
            end = max(end, last[s[i]])
            if i == end:
                ans.append(i - l + 1)
                l = i + 1
        return ans
        