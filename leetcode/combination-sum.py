class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        summ = 0
        combination, ans = [], []
        def backtrack(index):
            nonlocal summ, target
            if summ == target:
                ans.append(combination[:])
            if summ > target or candidates[index] > target:
                return 

            for i in range(index, len(candidates)):
                summ += candidates[i]
                combination.append(candidates[i])
                if summ <= target:
                    backtrack(i)

                combination.pop()
                summ -= candidates[i]
        backtrack(0)
        return ans
        