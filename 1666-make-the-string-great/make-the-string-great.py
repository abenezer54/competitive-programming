class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        n = len(s)
        for i in range(n):
            if stack and stack[-1].swapcase() == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        return ''.join(stack)
        