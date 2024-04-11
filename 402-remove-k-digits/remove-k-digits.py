class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        stack = deque()
        for i in range(n):
            while stack and stack[-1] > num[i] and k:
                stack.pop()
                k -= 1
            stack.append(num[i])

        while k and stack:
            stack.pop()
            k -= 1

        while stack and stack[0] == '0':
            stack.popleft()
            
        return ''.join(stack) if stack else '0'
        