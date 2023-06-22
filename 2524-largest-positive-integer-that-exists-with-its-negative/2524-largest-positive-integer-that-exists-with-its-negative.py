class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            x = abs(nums[i])
            if nums[i] < 0 and x in nums:
                return x
        return -1