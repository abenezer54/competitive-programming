class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        ind = [0] * n
        for a, b in edges:
            adj[a].append(b)
            ind[b] += 1
        ans = [set() for _ in range(n)]
        que = deque()
        for i in range(n):
            if not ind[i]:
                que.append(i)
        
        while que:
            node = que.popleft()
            for child in adj[node]:
                ans[child].add(node)
                ans[child].update(ans[node])
                ind[child] -= 1
                if not ind[child]:
                    que.append(child)
        ans = [sorted(row) for row in ans]
        return ans

        