class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n, stack = len(temp), []
        ans = [0] * n

        for i, val in enumerate(temp):
            while stack and temp[stack[-1]] < val:
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)
            
        return ans
        