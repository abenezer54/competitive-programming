class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        rem = set()
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            if s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    rem.add(i)
        rem.update(stack)

        ans = []
        for i in range(len(s)):
            if not i in rem:
                ans.append(s[i])
        return ''.join(ans)
        