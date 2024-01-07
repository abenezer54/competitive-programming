class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, zero, n = 0, 0, len(nums)
        ans = 0
        for r in range(n):
            if not nums[r]:
                zero += 1
            while zero > 1:
                if not nums[l]:
                    zero -= 1
                l += 1
            ans = max(ans, r - l)
        return ans

        