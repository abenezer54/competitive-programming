class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row_length = len(matrix)
        column_length = len(matrix[0])

        ans = [[0 for _ in range(row_length)] for _ in range(column_length)] 

        for i in range(row_length):
            for j in range(column_length):
                ans[j][i] = matrix[i][j]
                
        return ans
        