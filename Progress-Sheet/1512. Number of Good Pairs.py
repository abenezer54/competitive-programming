class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        #Using Dictionary
        dic = {}
        pair = 0
        for num in nums:
            if num in dic:
                pair += dic[num]
                dic[num] += 1     
            else:
                dic[num] = 1
        return pair
        #Using array itertation
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             count+= 1
        # return count
