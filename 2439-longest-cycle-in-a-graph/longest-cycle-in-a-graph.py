class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        adj = defaultdict(list)
        n = len(edges)
        for i in range(n):
            if edges[i] != -1:
                adj[i].append(edges[i])
                
        ans = -1
        col = [0] * n
        last = [0] * n
        dumb = 1
        for v in range(n):
            if not col[v]:
                stack = [v]
                col[v] = 1
                last[v] = dumb
                dumb += 1
                while stack:
                    flag = False
                    cur = stack[-1]
                    for u in adj[cur]:
                        if col[u] == 1:
                            ans = max(ans, dumb - last[u])
                            last[u] = dumb
                            dumb += 1
                        elif not col[u]:
                            flag = True
                            stack.append(u)
                            col[u] = 1
                            last[u] = dumb
                            dumb += 1

                    if not flag:
                        col[stack.pop()] = 2

        return ans
        