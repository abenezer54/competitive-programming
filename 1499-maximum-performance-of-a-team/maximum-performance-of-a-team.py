class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        a = sorted(zip(efficiency, speed), reverse=True)
        ans, tot, heap, mod = 0, 0, [], pow(10, 9) + 7
        for i in range(n):
            heappush(heap, a[i][1])
            tot += a[i][1]
            if len(heap) > k:
                tot -= heappop(heap)
            ans = max(ans, tot * a[i][0])
        return ans % mod