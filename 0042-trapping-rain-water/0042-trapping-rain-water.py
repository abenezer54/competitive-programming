class Solution:
    def trap(self, height: List[int]) -> int:      
        l = 0
        r = len(height) - 1
        lmax = height[l]
        rmax = height[r]
        ans = 0
        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                ans += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                ans += rmax - height[r] 
        return ans
