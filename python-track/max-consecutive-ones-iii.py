class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, zero, n = 0, 0, len(nums)
        ans = 0
        for r in range(n):
            if not nums[r]:
                zero += 1
            while zero > k:
                if not nums[l]:
                    zero -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
