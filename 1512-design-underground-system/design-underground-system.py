class UndergroundSystem:

    def __init__(self):
        self.waitList = defaultdict(list)
        self.TimeTaken = defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.waitList[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        stations = (self.waitList[id][0], stationName)
        time = t - self.waitList[id][1]
        self.TimeTaken[stations].append(time)

        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.TimeTaken[(startStation, endStation)]

        return sum(times) / len(times)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)