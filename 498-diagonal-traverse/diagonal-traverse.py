class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row_domain = {num for num in range(len(mat))}
        col_domain = {num for num in range(len(mat[0]))}
        direction = [-1, 1]
        current = [0, 0]
        ans = [mat[0][0]]

        while current[0] != len(mat) - 1 or current[1] != len(mat[0]) - 1: 
            previous = current.copy()
            current[0] += direction[0]
            current[1] += direction[1]
            if current[0] not in row_domain and current[1] not in col_domain:
                if current[0] < current[1]:
                    current = previous
                    current[0] += 1
                else:
                    current = previous
                    current[1] += 1
                direction[0] *= -1
                direction[1] *= -1
            elif current[0] not in row_domain:
                current = previous
                current[1] += 1
                direction[0] *= -1
                direction[1] *= -1
            elif current[1] not in col_domain:
                current = previous
                current[0] += 1
                direction[0] *= -1
                direction[1] *= -1

            ans.append(mat[current[0]][current[1]])

        return ans


        