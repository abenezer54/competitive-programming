class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, ans, cur_sum, n = 0, float("inf"), 0, len(nums)
        for r in range(n):
            cur_sum += nums[r]
            while cur_sum >= target:
                ans = min(ans, r - l + 1)
                cur_sum -= nums[l]
                l += 1
        if ans == float("inf"):
            return  0
        return ans      
        