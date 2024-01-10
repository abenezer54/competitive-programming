class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l, summ, cur, ans, n = 0, 0, set(), 0, len(nums)
        for r in range(n):
            while nums[r] in cur:
                cur.discard(nums[l])
                l += 1
            cur.add(nums[r])       
            ans = max(ans, sum(cur))
        return ans
        