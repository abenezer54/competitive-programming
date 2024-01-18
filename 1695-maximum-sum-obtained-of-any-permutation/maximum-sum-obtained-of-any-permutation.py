class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for start, final in requests:
            prefix[start] += 1
            prefix[final + 1] -= 1
        for i in range(1, n + 1):
            prefix[i] += prefix[i - 1]
            
        prefix = sorted(prefix, reverse=True)
        nums.sort(reverse=True)
        ans = 0
        for i in range(n):
            ans += nums[i] * prefix[i]
        return (ans %(10 ** 9 + 7))
        