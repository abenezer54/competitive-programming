class Solution:
    def reverseParentheses(self, s: str) -> str:
        s = list(s)
        stack = []
        for i, char in enumerate(s):
            if char == ")":
                s = s[:stack[-1] + 1] + s[stack[-1] + 1:i][::-1] + s[i:]
                stack.pop() 
            elif char == "(":
                stack.append(i)   
        ans = [char for char in s if char != ")" and char != "("]

        return "".join(ans)
                
        