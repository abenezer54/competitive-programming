class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        conc = 0
        l = 0
        r = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        else:
            while l < r:
                conc += int(str(nums[l]) + str(nums[r]))
                l += 1
                r -= 1
            if len(nums) % 2 != 0:
                conc += nums[len(nums)//2]
        return conc
