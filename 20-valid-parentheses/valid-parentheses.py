class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        look = {")" : "(", "]" : "[", "}" : "{"}
        
        for char in s:
            if char not in look:
                stack.append(char)
            else:
                if stack and stack[-1] == look[char]:
                    stack.pop()
                else:
                    return False

        return not stack
                
