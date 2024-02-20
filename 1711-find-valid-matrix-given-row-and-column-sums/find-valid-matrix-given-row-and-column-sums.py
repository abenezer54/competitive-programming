class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n, m = len(rowSum), len(colSum)
        ans = [[0] * m for _ in range(n)]  
        for row in range(n):
            for col in range(m):
                minn = min(rowSum[row], colSum[col]) 
                ans[row][col] = minn
                rowSum[row] -= minn
                colSum[col] -= minn
        return ans
