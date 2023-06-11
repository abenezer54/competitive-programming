class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        print(nums)
        ans = []
        for q in range(len(queries)):
            summ = 0
            i = 0
            while i < len(nums) and summ + nums[i] <= queries[q]:
                summ += nums[i]
                i += 1              
            ans.append(i)
        return ans
