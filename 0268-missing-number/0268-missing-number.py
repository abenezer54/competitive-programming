class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(list(set(nums)))
        ans = 0
        for i in range(n+1):
            if not i in nums:
                ans = i
                break
        return ans