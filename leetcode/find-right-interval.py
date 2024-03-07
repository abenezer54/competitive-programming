class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        sorted_start = sorted([[intervals[i][0], i] for i in range(n)])
        ans = [-1] * n

        for i in range(n):
            start, end = intervals[i]
            left, right = -1, n - 1
            idx = sorted_start[-1][-1]

            while left + 1 < right:
                mid = (left + right) // 2
                if sorted_start[mid][0] >= end:
                    right = mid
                    idx = sorted_start[mid][1]
                else:
                    left = mid
            if intervals[idx][0] >= end:
                ans[i] = idx
                
        return ans
        