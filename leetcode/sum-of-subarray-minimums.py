class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n, stack = len(arr), []
        nxt = [n] * n
        prev = [-1] * n
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                top = stack.pop()
                nxt[top] = i

            if stack:
                prev[i] = stack[-1]
            stack.append(i)

        ans = 0
        for i in range(n):
            left_len = i - prev[i]
            right_len = nxt[i] - i
            tot = left_len * right_len
            ans = (ans + (tot * arr[i])) % (10**9 + 7) 

        return ans 
        