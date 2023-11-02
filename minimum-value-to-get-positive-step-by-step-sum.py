class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        N = len(nums)
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i + 1] = prefix[i] + nums[i]
        prefix.remove(0)

        if min(prefix) < 0:
            return abs(min(prefix)) + 1

        return 1