class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n, m = len(rowSum), len(colSum) 
        ans = [[0]* m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                mn = min(rowSum[i], colSum[j])
                ans[i][j] = mn
                rowSum[i] -= mn
                colSum[j] -= mn
        return ans
        