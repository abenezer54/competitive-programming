class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        currentSum = 0
        minValue = float("inf")
        for i in range(len(nums)):
            currentSum += nums[i]
            minValue = min(minValue, currentSum)
            
        if minValue < 1:
            return abs(minValue) + 1
        return 1