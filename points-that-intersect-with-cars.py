class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        arr = []
        for row in nums:
            for i in range(row[0], row[1] + 1):
                if i not in arr:
                    arr.append(i)

        return len(arr)