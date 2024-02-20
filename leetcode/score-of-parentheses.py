class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        ans = 0

        for i, c in enumerate(s):
            if c == "(":
                stack.append(c)
            else:
                stack.pop()
                if s[i - 1] == '(':
                    ans += pow(2, len(stack))

        return ans