class ATM:
    def __init__(self):
        self.count = defaultdict(int)
        self.look = [20, 50, 100, 200, 500]


    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.count[self.look[i]] += banknotesCount[i]


    def withdraw(self, amount: int) -> List[int]:
        ans = [0] * 5 
        for i in range(4, -1, -1):
            cur_need = amount // self.look[i]
            if cur_need >= self.count[self.look[i]]:
                ans[i] = self.count[self.look[i]]
                amount -= self.count[self.look[i]] * self.look[i]
            else:
                ans[i] = cur_need
                amount -= cur_need * self.look[i]
                
            if amount == 0:
                for i in range(5):
                    self.count[self.look[i]] -= ans[i]
                return ans
        else:
            return [-1]
        