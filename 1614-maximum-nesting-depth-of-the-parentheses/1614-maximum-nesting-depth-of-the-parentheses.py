class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        ans = 0
        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")":
                ans = max(ans, len(stack))
                stack.pop()
            else:
                ans = max(ans, len(stack))

        return ans