class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = cur_sum = 0
        count = Counter()
        count[0] = 1
        for i in range(n):
            cur_sum += nums[i]
            diff = cur_sum - k
            ans += count[diff]
            count[cur_sum] += 1
        return ans
        