class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k = nums.count(1)
        if not k:
            return 0
        l, zero, ans, n = 0, 0, float("inf"), len(nums)
        nums *= 2

        for r in range(n * 2):
            if not nums[r]:
                zero += 1
            if r >= k - 1:
                ans = min(ans, zero)
                if not nums[l]:
                    zero -= 1
                l += 1
        return ans                     