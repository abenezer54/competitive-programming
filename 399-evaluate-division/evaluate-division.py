class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)
        adj = defaultdict(list)
        for i in range(n):
            adj[equations[i][0]].append((equations[i][1], values[i]))
            adj[equations[i][1]].append((equations[i][0], 1 / values[i]))
        
        def dfs(u, v, p, par):
            vis.add(u)
            if u == v: return p

            for node, val in adj[u]:
                if node != par and  node not in vis:
                    res = dfs(node, v, p * val, u)
                    if res != -1:
                        return res
            return -1 

        ans = []
        for u, v in queries:
            if not u in adj or not v in adj:
                ans.append(-1)
                continue
            vis = set()
            ans.append(dfs(u, v, 1, 0))
        return ans            

