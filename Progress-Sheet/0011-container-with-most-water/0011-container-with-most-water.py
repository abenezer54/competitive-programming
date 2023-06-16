class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        maxx = 0
        while l < r:
            width = r - l
            length = min(height[l], height[r])
            a = length * width
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
            if a > maxx:
                maxx = a
        return maxx
                

        