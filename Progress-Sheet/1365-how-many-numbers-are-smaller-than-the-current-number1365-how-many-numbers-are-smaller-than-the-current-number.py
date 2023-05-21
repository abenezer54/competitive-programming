class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic = {}
        arr = []
        #with using array which is not efficient
        # for i in range(len(nums)) :      
        #     count = 0
        #     for j in range(len(nums)):
        #         if nums[i] > nums[j]:
        #             count += 1
        #     arr.append(count)
        
        #Using dictionary
        sortedArr = sorted(nums)
        for i in range(len(nums)):
            if sortedArr[i] not in dic:
                dic[sortedArr[i]] = i
        for i in nums:
            arr.append(dic[i])
        return arr
                
