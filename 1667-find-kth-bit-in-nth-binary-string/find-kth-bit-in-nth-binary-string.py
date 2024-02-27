class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def find(n, k):
            mid = pow(2, n - 1)

            if n == 1:
                return 0
            if k == mid:
                return 1
            if k > mid:
                return 1 - find(n - 1, (mid - (k - mid)))
            else:
                return find(n - 1, k)
        return str(find(n, k))
        