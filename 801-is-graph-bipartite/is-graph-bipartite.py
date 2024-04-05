class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        col = [-1] * n
        for v in range(n):
            if col[v] == -1:
                stack = [(v, 0)]
                col[v] = 0
                while stack:
                    v, c = stack.pop()
                    for u in graph[v]:
                        if col[u] == -1:
                            stack.append((u, 1 - c))
                            col[u] = 1 - c
                        elif col[u] == c:
                            return False
        return True

        