class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []
        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                if diff <= bricks:
                    bricks -= diff
                    heappush(heap, -diff)
                else:
                    if ladders <= 0:
                        return i
                    else:
                        ladders -= 1
                        heappush(heap, -diff)
                        bricks += -heappop(heap)
                        bricks -= diff

        return n - 1
                    