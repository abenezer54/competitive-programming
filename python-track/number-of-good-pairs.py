class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        ans = 0
        for num in nums:
            if num in seen:
                ans += seen[num]
            seen[num] += 1
        return ans
        