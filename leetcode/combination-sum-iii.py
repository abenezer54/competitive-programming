class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        tot, comb, ans = 0, [], []
        def backtrack(start):
            nonlocal tot
            if tot == n and len(comb) == k:
                ans.append(comb.copy())
            if tot > n:
                return

            for num in range(start, 10):
                comb.append(num)
                tot += num
                backtrack(num + 1)
                tot -= comb.pop()
        backtrack(1)
        return ans
        