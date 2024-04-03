class Solution:
    def findCircleNum(self, graph: List[List[int]]) -> int:
        adj = defaultdict(list)
        n, m = len(graph), len(graph[0])
        for i in range(n):
            for j in range(m):
                if i != j and graph[i][j]:
                    adj[i].append(j)
                    
        vis = [0] * n
        ans = 0
        for v in range(n):
            if not vis[v]:
                ans += 1
                stack = [v]
                vis[v] = 1
                while stack:
                    top = stack.pop()
                    for u in adj[top]:
                        if not vis[u]:
                            vis[u] = 1
                            stack.append(u)
        return ans
        