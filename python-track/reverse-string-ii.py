class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverseUptoK(s, i, k):
            while i < k:
                s[i], s[k] = s[k], s[i]
                i += 1
                k -= 1

        s = list(s)
        N = len(s)
        for index in range(0, N, 2 * k):
            reverseUptoK(s, index, min(N - 1, index + k - 1))

        return "".join(s)
        