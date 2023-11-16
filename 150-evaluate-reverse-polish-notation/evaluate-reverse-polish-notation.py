class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if not char in ["*", "/", "+", "-"]:
                stack.append(int(char))
            else:
                if char == "*":
                    stack[-2] = stack[-2] * stack[-1]
                    stack.pop()
                elif char == "/":
                    stack[-2] = int(stack[-2] / stack[-1])
                    stack.pop()
                elif char == "+":
                    stack[-2] = stack[-2] + stack[-1]
                    stack.pop()
                elif char == "-":
                    stack[-2] = stack[-2] - stack[-1]
                    stack.pop()
        return stack[0]