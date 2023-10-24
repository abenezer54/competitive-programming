class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operation(operator, a, b):
            if operator == "+":
                return a + b
            elif operator == "-":
                return a - b
            elif operator == "*":
                return a * b
            elif operator == "/":
                return int(a / b)
            else:
                raise ValueError("Invalid operator")

        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                res = operation(token, stack[-2], stack[-1])
                stack.pop()
                stack[-1] = res
        return stack[0]