class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        l = 0
        ans = -float("inf")
        cur_sum = 0
        for r in range(n):
            cur_sum += nums[r]
            if r >= k - 1:
                ans = max(ans, cur_sum / k)
                cur_sum -= nums[l]
                l += 1
                
        return ans
        