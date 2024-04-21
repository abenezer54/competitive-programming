class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        heappush(self.large, num)

        if (self.small and self.large and self.large[0] < -self.small[0]) or (len(self.large) > len(self.small) + 1):
            x = heappop(self.large)
            heappush(self.small, -x)
        if len(self.small) > len(self.large) + 1:
            x = -heappop(self.small)
            heappush(self.large, x)
        

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]

        if len(self.small) > len(self.large):
            return -self.small[0]

        return (-self.small[0] + self.large[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()