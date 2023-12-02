class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = set(nums)
        s.discard(0) if 0 in s else s
        return len(s)