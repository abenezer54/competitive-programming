class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        temp = []
        for key, value in dic.items():
            temp.append([key, value])
        ans = 0
        for i in temp:
            if i[1] == 1:
                ans += i[0]
        return ans