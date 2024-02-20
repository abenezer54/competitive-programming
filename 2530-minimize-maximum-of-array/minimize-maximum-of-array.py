class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n, cur, ans = len(nums), 0, 0
        for i in range(n):
            cur += nums[i]
            ans = max(ans, (cur + i)// (i + 1))
        return ans
