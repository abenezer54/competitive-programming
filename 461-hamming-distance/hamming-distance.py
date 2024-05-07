class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = format(x, 'b')
        y = format(y, 'b')
        ans = 0
        for i in range(1, min(len(x), len(y)) + 1):
            if x[-i] != y[-i]:
                ans += 1
        return ans + x[:-i].count('1') + y[:-i].count('1')
        