class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap, n, i = [], len(profits), 0
        a = sorted(zip(capital, profits))
        for _ in range(k):
            while i < n and w >= a[i][0]:
                heappush(heap, -a[i][1])
                i += 1
            if heap:
                w += -heappop(heap)
        return w
        