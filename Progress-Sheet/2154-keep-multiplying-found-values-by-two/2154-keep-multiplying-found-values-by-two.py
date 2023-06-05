class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        for i in range(len(nums)):
            if original in nums:
                original*=2
        else:
            return original