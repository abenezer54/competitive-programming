class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = [0, 0, 0]
        for i in nums:
            arr[i] += 1
        nums[0:arr[0]] = [0] * arr[0]
        nums[arr[0] : arr[0] + arr[1]] = [1] * arr[1]
        nums[arr[0] + arr[1] : arr[0] + arr[1] + arr[2]] = [2] * arr[2]
        print(nums)
            
        
