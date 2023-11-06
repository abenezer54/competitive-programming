class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_average = -float("inf")
        current_sum = 0
        for right, num in enumerate(nums):
            current_sum += num
            if right - k + 1 >= 0:
                max_average = max(max_average, (current_sum/k))
                current_sum -= nums[right - k + 1]
                
        return max_average