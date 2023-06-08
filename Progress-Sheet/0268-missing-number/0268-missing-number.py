class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = set(nums)
        for i in range(len(n)+1):
            if not i in n:
                return i
