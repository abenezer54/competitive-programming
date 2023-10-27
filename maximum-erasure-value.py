class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        unique_set = set()
        ans = 0
        left = 0
        current_sum = 0
        for right, num in enumerate(nums):
            while num in unique_set:
                unique_set.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            unique_set.add(num)
            current_sum += num
            ans = max(ans, current_sum)

        return ans