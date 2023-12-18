class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = [0, 0]
        arr = []
        for row in grid:
            arr.extend(row)
        count = Counter(arr)
        for k, v in count.items():
            if v == 2:
                ans[0] = k
                break
            
        a = set(arr)
        for i in range(1, len(grid)**2 + 1):
            if i not in a:
                ans[1] = i
                break

        return ans
        