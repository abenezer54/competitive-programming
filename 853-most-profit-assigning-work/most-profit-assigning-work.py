class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n, m = len(profit), len(worker)
        a =[[0, 0]] + [[difficulty[i], profit[i]] for i in range(n)]
        a.sort()
        for i in range(1, n + 1):
            a[i][1] = max(a[i][1], a[i - 1][1])

        ans = 0
        for i in range(m):
            l, r = 0, n + 1
            while l + 1 < r:
                mid = (l + r) // 2
                if a[mid][0] <= worker[i]:
                    l = mid
                else:
                    r = mid
            ans += a[l][1]
        return ans
