class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()       
        arr = []
        for i in range(len(nums)//2):
            arr.append([nums[i], nums[len(nums)-i-1]])
        return sum(max(arr, key = lambda x: sum(x)))