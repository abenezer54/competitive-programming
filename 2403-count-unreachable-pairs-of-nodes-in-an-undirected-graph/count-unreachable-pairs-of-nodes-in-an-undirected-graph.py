class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        vis = [0] * n
        adj = [[] for _ in range(n)]
        
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        arr = []
        for v in range(n):
            if vis[v] == 0:
                stack = [v]
                vis[v] = 1
                cur = 0
                while stack:
                    cur += 1
                    node = stack.pop()
                    for nei in adj[node]:
                        if vis[nei] == 0:
                            stack.append(nei)
                            vis[nei] = 1
                arr.append(cur)

        ans, sm = 0, arr[0]
        for i in range(1, len(arr)):
            ans += sm * arr[i]
            sm += arr[i]
        
        return ans
    