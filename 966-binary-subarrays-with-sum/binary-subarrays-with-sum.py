class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cur_sum = ans = 0
        count = Counter()
        count[0] = 1
        for i in range(len(nums)):
            cur_sum += nums[i]
            ans += count[cur_sum - goal]
            count[cur_sum] += 1
        return ans