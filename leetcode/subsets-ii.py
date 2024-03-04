class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(current_index):
            ans.add(tuple(sorted(subset.copy())))

            for candidate in range(current_index, len(nums)):
                subset.append(nums[candidate])
                backtrack(candidate + 1)
                subset.pop()

        ans, subset = set(), []
        backtrack(0)      
        return list(ans)
        