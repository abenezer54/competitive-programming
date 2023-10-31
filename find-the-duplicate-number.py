class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if not num in dic:
                dic[num] = 1
            else:
                return num