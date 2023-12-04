class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums.append(0)
        ans = 0
        cur = 0
        for num in nums:
            if num:
                cur += 1
                ans = max(ans, cur)
            else:
                cur = 0
        return ans