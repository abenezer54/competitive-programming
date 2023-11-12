class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        maxx = 0
        count = 0
        for right, num in enumerate(nums):
            if not num:
                count += 1
            while count > 1:
                if not nums[left]:
                    count -= 1
                left += 1
            maxx = max(maxx, right - left)
            
        return maxx