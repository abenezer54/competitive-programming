class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        visited = defaultdict(int)
        def find(row, col):
            if col == 0 or row == col:
                return 1
            if col == 1 or col == row - 1:
                return row
            if (row, col) not in visited:
                visited[(row, col)] = find(row - 1, col - 1) + find(row - 1, col)
            return visited[(row, col)]
        ans = [[find(row, i) for i in range(row + 1)] for row in range(numRows)]     

        return ans