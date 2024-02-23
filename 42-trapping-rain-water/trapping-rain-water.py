class Solution:
    def trap(self, height: List[int]) -> int:
        n, stack, ans = len(height), [], 0
        for r in range(n):
            while stack and height[stack[-1]] <= height[r]:
                top = stack.pop()
                if stack:
                    h = min(height[stack[-1]], height[r]) - height[top]
                    w = r - stack[-1] - 1
                    ans += h * w
            stack.append(r)
        return ans
        