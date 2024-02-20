class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = list(filter(None, re.split("/+", path)))
        n = len(arr)
        stack = []
        for i in range(n):
            if arr[i] == "..":
                if stack:
                    stack.pop()
            elif arr[i] == '.':
                continue
            else:
                stack.append(arr[i])

        return '/' + "/".join(stack)
        