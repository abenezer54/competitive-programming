class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = [] 
        i = 0
        n = len(nums) - 1
        while len(arr) != len(nums):
            arr.append(nums[i])
            i += 1
            
            if i <= n:
                arr.append(nums[n])
                n -= 1
        return arr
            