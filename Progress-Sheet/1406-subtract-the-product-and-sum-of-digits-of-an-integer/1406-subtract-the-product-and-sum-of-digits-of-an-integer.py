class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        strs = str(n)
        product = 1
        summ = 0
        for i in range(len(strs)):
            product *=  int(strs[i])
        for i in range(len(strs)):
            summ += int(strs[i])

        return product - summ