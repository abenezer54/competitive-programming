class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = [0]
        for i in range(len(nums)):
            arr.append(nums[i] +arr[i])
        arr.remove(0)
        return arr