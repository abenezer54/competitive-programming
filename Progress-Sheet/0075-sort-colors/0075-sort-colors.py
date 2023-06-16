class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lp = 0
        rp = len(nums) - 1
        s = 0
        while s < len(nums) and s <= rp:
            if nums[s] == 2:
                nums[rp], nums[s] = nums[s], nums[rp]
                rp -= 1
                s -= 1
            elif nums[s] == 0:
                nums[lp], nums[s] = nums[s], nums[lp]
                lp += 1
            s += 1