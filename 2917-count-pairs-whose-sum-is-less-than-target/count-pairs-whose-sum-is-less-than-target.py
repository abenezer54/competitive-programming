class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()

        left = 0 
        right = n - 1
        ans = 0
        while left < right:
            cur_sum = nums[left] + nums[right]
            if cur_sum < target:
                ans += right - left 
                left += 1
            else:
                right -= 1
        return ans
        