class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxLength = 0
        left = 0
        count = 0
        for right, num in enumerate(nums):
            if not num:
                count += 1
            if count > k:
                if not nums[left]:
                    count -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)

        return maxLength
        