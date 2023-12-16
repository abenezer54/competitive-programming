class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        maxOfColumn = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                maxOfColumn[j] = max(maxOfColumn[j], matrix[i][j])
        
        ans = []
        for i in range(len(matrix)):
            minn = min(matrix[i])
            for j in range(len(matrix[i])):
                if matrix[i][j] == minn and matrix[i][j] == maxOfColumn[j]:
                    ans.append(matrix[i][j])
        
        return ans
        