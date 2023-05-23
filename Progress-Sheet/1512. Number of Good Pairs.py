class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        #Using Counter from Collections and Arithmetic sum to find the number of pairs
        from collections import Counter
        count = 0
        dic = Counter(nums) #counts the number of repitions for each unique keys
        for i in dic.values():
            count += (i * (i-1))//2 #formula to find pairs with number of repititons 
        return count
        #Using Dictionary
        # dic = {}
        # pair = 0
        # for num in nums:
        #     if num in dic:
        #         pair += dic[num]
        #         dic[num] += 1     
        #     else:
        #         dic[num] = 1
        # return pair
        #Using array itertation
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             count+= 1
        # return count
