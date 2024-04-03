class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        vis = [-1] * n
        for v in range(n):
            if vis[v] == -1:
                stack = [(v, 0)]
                while stack:
                    node, col = stack.pop()
                    for u in graph[node]:
                        if vis[u] != -1:
                            if vis[u] == col:
                                return False
                        else:
                            vis[u] = col ^ 1
                            stack.append((u, col ^ 1))
        return True                   
        