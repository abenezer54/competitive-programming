class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key = lambda arr:arr[0])
        maximum_difference = 0
        for i in range(len(points) - 1):
            current_difference = points[i + 1][0] - points[i][0]
            maximum_difference = max(maximum_difference, current_difference)
            
        return maximum_difference
        