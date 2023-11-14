class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        maxValue = 0
        for start, end in nums:
            maxValue = max(end, maxValue)

        prefix = [0] * (maxValue + 2)
        for start, end in nums:
            prefix[start] += 1
            prefix[end + 1] -= 1

        for i in range(1, maxValue + 1):
            prefix[i] = prefix[i] + prefix[i - 1]

        ans = 0
        for num in prefix:
            if num > 0:
                ans += 1
        return ans
        