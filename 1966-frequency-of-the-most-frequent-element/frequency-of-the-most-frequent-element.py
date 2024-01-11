class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, count, ans, n = 0, 0, 1, len(nums)

        for r in range(n):
            cur = (nums[r] - nums[r - 1]) * (r - l)
            count += cur
            while count > k:
                count -= nums[r] - nums[l]
                l += 1
            ans = max(ans, r - l + 1)

        return ans