class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        domain = set(range(len(nums) + 1))
        return (domain - set(nums)).pop()     