class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:  
        if not self.hashmap[key]:
            return ''     
        left, right = 0, len(self.hashmap[key])
        while left + 1 < right:
            mid = (left + right) // 2
            if self.hashmap[key][mid][1] <= timestamp:
                left = mid
            else:
                right = mid

        return self.hashmap[key][left][0] if self.hashmap[key][left][1] <= timestamp else ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)