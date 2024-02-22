class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        n = len(arr)
        stack = []
        for i in range(n):
            if arr[i] == "..":
                if stack:
                    stack.pop()
            elif arr[i] == '.' or arr[i] == '':
                continue
            else:
                stack.append(arr[i])

        return '/' + "/".join(stack)
        