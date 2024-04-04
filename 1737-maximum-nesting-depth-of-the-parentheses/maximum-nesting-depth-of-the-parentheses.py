class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        n = len(s)
        ans = 0
        for i in range(n):
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] == ')':
                stack.pop()
            ans = max(ans, len(stack))
        return ans
        