class FrequencyTracker:

    def __init__(self):
        self.counter = defaultdict(int)
        self.frequencyCounter = defaultdict(int)      

    def add(self, number: int) -> None:
        self.counter[number] += 1
        self.frequencyCounter[self.counter[number]] += 1
        if self.frequencyCounter[self.counter[number] - 1] > 0:
            self.frequencyCounter[self.counter[number] - 1] -= 1      

    def deleteOne(self, number: int) -> None:
        if self.counter[number] > 0:
            self.frequencyCounter[self.counter[number] - 1] += 1
            self.frequencyCounter[self.counter[number]] -= 1
            self.counter[number] -= 1

    def hasFrequency(self, frequency: int) -> bool:
        if self.frequencyCounter[frequency] > 0:
            return True
            
        return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)