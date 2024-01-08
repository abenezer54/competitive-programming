class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, n = 0, len(nums)
        for r in range(n):
            if nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return l 
        