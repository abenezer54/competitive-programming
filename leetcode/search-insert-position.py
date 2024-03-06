class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = bisect_right(nums, target)
        if idx - 1 >= 0 and nums[idx - 1] == target:
            return idx - 1
        return idx
