class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.look = {}

    def insert(self, val: int) -> bool:
        if val in self.look:
            return False

        self.arr.append(val)
        self.look[val] = len(self.arr) - 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.look:
            return False

        idx = self.look[val]
        self.look[self.arr[-1]] = idx
        self.arr[-1], self.arr[idx] = self.arr[idx], self.arr[-1]
        self.arr.pop()
        self.look.pop(val)
        
        return True

    def getRandom(self) -> int:
        
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()