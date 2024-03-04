class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combination, ans = [], set()
        summ = 0
        def backtrack(index, prev):
            nonlocal target, summ
            if summ == target:
                ans.add(tuple(combination.copy()))
                return 
            if summ > target or (index < len(candidates)  and candidates[index] == prev):
                return 
            for i in range(index, len(candidates)):
                combination.append(candidates[i])
                summ += candidates[i]
                if summ <= target:
                    backtrack(i + 1, prev)
                prev = combination.pop()
                summ -= candidates[i]

        backtrack(0, -1)
        return list(ans)