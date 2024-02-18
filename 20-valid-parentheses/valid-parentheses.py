class Solution:
    def isValid(self, s: str) -> bool:
        look  = {")": "(", "]" : "[", "}" : "{"}
        stack = []
        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(char)
            elif stack and stack[-1] == look[char]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True
        