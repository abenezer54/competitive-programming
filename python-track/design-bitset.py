class Bitset:

    def __init__(self, size: int):
        self.length = size 
        self.arr = [False] * size 
        self.flipped = [True] * size
        self.oneCount = 0

        
    def fix(self, idx: int) -> None:
        if not self.arr[idx]:
            self.arr[idx] = True
            self.flipped[idx] =False
            self.oneCount += 1


    def unfix(self, idx: int) -> None:
        if self.arr[idx]:
            self.arr[idx] = False
            self.flipped[idx] = True
            self.oneCount -= 1


    def flip(self) -> None:
        self.arr, self.flipped = self.flipped, self.arr
        self.oneCount = self.length - self.oneCount


    def all(self) -> bool:      
        return self.length == self.oneCount


    def one(self) -> bool:
        return self.oneCount > 0


    def count(self) -> int:
        return self.oneCount


    def toString(self) -> str:
        return "".join("1" if bit else "0" for bit in self.arr)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()