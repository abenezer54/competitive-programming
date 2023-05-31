class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digitSum = 0
        for i in nums:
            for digit in str(i):
                digitSum += int(digit)      
        return abs(sum(nums) - digitSum)