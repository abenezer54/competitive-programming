class Solution:
    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        for a, b in pre:
            adj[b].append(a)
            indegree[a] += 1
        que = deque()
        for v in range(n):
            if not indegree[v]:
                que.append(v)
        ans = []
        while que:
            node = que.popleft()
            ans.append(node)
            for child in adj[node]:
                indegree[child] -= 1
                if not indegree[child]:
                    que.append(child)
            
        return ans if len(ans) == n else []
        