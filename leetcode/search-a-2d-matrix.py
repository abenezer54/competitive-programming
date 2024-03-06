class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        l, r = 0, n 
        while l + 1 < r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target:
                l = mid
            else:
                r = mid
        row = l
        
        l, r = 0, m 
        while l + 1 < r:
            mid = (l + r) // 2
            if matrix[row][mid] <= target:
                l = mid
            else:
                r = mid

        return matrix[row][l] == target
        