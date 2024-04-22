class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj = [[] for _ in range(n)]
        out = [0] * n
        que = deque()
        for i in range(n):
            out[i] = len(graph[i])
            if not graph[i]:
                que.append(i)
            for v in graph[i]:
                adj[v].append(i)

        ans = []
        while que:
            v = que.popleft()
            ans.append(v)
            for u in adj[v]:
                out[u] -= 1

                if not out[u]:
                    que.append(u)

        return sorted(ans)
        