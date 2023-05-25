class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            rs = sum(nums[i+1:])
            ls = sum(nums[:i]) 
            answer.append(abs(ls - rs))
        return answer
                
        