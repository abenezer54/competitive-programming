class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        fall = 0
        for char in s:
            if char == "(":
                stack.append(char)
            else:
                if stack:
                    stack.pop()
                else:
                    fall += 1

        return len(stack) + fall