class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = nums.count(0)
        o = nums.count(1) + z

        for i in range(len(nums)):
            if i < z:
                nums[i] = 0
            elif i < o:
                nums[i] = 1
            else:
                nums[i] = 2
