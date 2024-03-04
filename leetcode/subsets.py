class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(current_index):
            ans.append(subset.copy())

            for candidate in range(current_index, len(nums)):
                subset.append(nums[candidate])
                backtrack(candidate + 1)
                subset.pop()

        ans, subset = [], []
        backtrack(0)      
        return ans
        