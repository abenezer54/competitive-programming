class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        left = 0
        zero_count = 0
        for right, num in enumerate(nums):
            if num == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            ans = max(ans, right - left)
        
        return ans