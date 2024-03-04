class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(current_num):
            nonlocal n
            if len(combination) == k:
                ans.append(combination.copy())
                return 
            
            for candidate in range(current_num, n + 1):
                combination.append(candidate)
                backtrack(candidate + 1)
                combination.pop()

        ans, combination = [], []
        backtrack(1)
        return ans
        