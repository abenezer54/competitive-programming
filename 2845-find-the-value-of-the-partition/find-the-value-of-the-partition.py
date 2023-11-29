class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        minn = float("inf")
        for i in range(1, len(nums)):
            diff = abs(nums[i] - nums[i-1])
            if diff < minn:
                minn = diff
        return minn