class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x = nums[0]
        for i in range(1, len(nums)):
            x ^= nums[i]
        return (x ^ k).bit_count()