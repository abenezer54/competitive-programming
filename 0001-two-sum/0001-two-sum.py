class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       dic = {}
       for i in range(len(nums)):
            if not target - nums[i] in dic:
               dic[nums[i]] = i
            else:
                return [i , dic[target - nums[i]]]
