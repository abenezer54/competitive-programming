class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def find(n, k):
            if n == 1:
                return 0

            if k & 1:
                return find(n - 1, (k + 1) // 2)
            else:
                return 1 - find(n - 1, (k + 1) // 2)
        return find(n, k)
        