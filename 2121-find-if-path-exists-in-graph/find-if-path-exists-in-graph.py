class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination: return True
        adj = defaultdict(list)
        vis = [0] * n
        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)

        stack = [source]
        vis[source] = 1
        while stack:
            top = stack.pop()
            for child in adj[top]:
                if child == destination:
                    return True
                if not vis[child]:
                    stack.append(child)
                    vis[child] = 1
        return False
        