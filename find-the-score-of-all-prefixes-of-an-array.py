class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        N = len(nums)
        conver = [0] * N
        maxx = 0
        for i, num in enumerate(nums):
            maxx = max(maxx, num)
            conver[i] = maxx + num
            if i > 0:
                conver[i] = conver[i] + conver[i-1]

        return conver