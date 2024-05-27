class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for x in range(len(nums) + 1):
            if len(nums) - bisect_left(nums, x) == x:
                return x
        return -1
        