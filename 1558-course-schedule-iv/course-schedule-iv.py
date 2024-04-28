class Solution:
    def checkIfPrerequisite(self, n: int, pre: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(n)]
        ind = [0] * n
        for a, b in pre:
            adj[a].append(b)
            ind[b] += 1
        req = defaultdict(set)
        que = deque()
        for i in range(n):
            if not ind[i]:
                que.append(i)
        
        while que:
            node = que.popleft()
            for child in adj[node]:
                ind[child] -= 1
                req[child].add(node)
                req[child].update(req[node])
                if not ind[child]:
                    que.append(child)
        
        ans = []
        for a, b in queries:
            if a in req[b]:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans
        