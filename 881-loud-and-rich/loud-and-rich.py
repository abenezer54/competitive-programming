class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        ans = list(range(n))
        adj = [[] for _ in range(n)]
        ind = [0] * n
        for a, b in richer:
            adj[a].append(b)
            ind[b] += 1

        que = deque()
        for i in range(n):
            if not ind[i]:
                que.append(i)
        
        while que:
            node = que.popleft()
            for child in adj[node]:
                ind[child] -= 1
                if quiet[ans[child]] > quiet[ans[node]]:
                    ans[child] = ans[node]
                if not ind[child]:
                    que.append(child)
        return ans