class Solution:
    def canFinish(self, n: int, pre: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in pre:
            adj[u].append(v)
        col = [0] * n 
        for v in range(n):
            if not col[v]:
                stack = [v]          
                while stack:             
                    col[stack[-1]] = 1
                    flag = False
                    for u in adj[stack[-1]]:
                        if not col[u]:
                            stack.append(u)
                            flag = True
                        if col[u] == 1:
                            return False
                    if not flag:
                        top = stack.pop()
                        col[top] = 2

        return True
        