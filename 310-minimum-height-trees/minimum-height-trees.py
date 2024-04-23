class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        ind = [0] * n
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            ind[a] += 1
            ind[b] += 1

        que = deque()
        cnt = 0
        for i in range(n):
            if ind[i] == 1:
                que.append(i)
                cnt += 1

        ans = []
        while que:
            l = len(que)
            if cnt == n:
                return list(que) 
            for _ in range(l):
                v = que.popleft()
                for u in adj[v]:
                    ind[u] -= 1
                    if ind[u] == 1:
                        que.append(u)
                        cnt += 1

        return [0]
