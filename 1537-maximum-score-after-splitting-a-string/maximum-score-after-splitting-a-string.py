class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        zero = [0] * (n + 1)
        one = [0] * (n + 1)
        for i in range(n):
            if s[i] == '0':
                zero[i + 1] = zero[i] + 1
            else:
                zero[i + 1] = zero[i]

        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                one[i] = one[i + 1] + 1
            else:
                one[i] = one[i + 1]

        maxx = 0
        for i in range(n - 1):
            cur = zero[i + 1] + one[i + 1]
            maxx = max(maxx, cur)

        return maxx
        