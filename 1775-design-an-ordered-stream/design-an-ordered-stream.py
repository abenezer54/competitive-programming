class OrderedStream:

    def __init__(self, n: int):
        self.stream = [""] * n
        self.ptr = 0
        self.n = n


    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value
        ans = []
        while self.ptr < self.n and self.stream[self.ptr]:
            ans.append(self.stream[self.ptr])
            self.ptr += 1
            
        return ans
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)