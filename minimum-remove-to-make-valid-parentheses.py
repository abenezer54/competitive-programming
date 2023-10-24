class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = [char for char in s]

        for i, char in enumerate(s):
            if char == "(":
                stack.append(char)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""

        j = len(s) - 1
        while len(stack) > 0:
            print(j)
            if s[j] == stack[-1]:
                stack.pop()
                s.pop(j)
            j -= 1

        return "".join(s)