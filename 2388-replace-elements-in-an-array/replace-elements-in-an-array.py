class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hashmap = {nums[i]: i for i in range(len(nums))}

        for previous_num, new_num in operations:
            nums[hashmap[previous_num]] = new_num    
            hashmap[new_num] = hashmap[previous_num]
            hashmap.pop(previous_num)
            
        return nums
        