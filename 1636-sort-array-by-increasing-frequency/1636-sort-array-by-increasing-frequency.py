# from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sorted(sorted(nums, reverse=True), key=nums.count)

            
        