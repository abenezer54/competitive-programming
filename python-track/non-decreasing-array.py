class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if i >= 1 and nums[i + 1] < nums[i - 1]:
                    count += 1
                    nums[i + 1] = nums[i]
                else:
                    count += 1
                    nums[i] = nums[i + 1]
        return count < 2
        