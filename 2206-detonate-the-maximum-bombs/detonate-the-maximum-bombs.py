class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(bombs)
        for i in range(n):
            for j in range(i + 1, n):
                x = pow(abs(bombs[i][0] - bombs[j][0]), 2)
                y = pow(abs(bombs[i][1] - bombs[j][1]), 2)
                d = sqrt(x + y)
                if d <= bombs[i][2]:
                    adj[i].append(j)
                if d <= bombs[j][2]:
                    adj[j].append(i)
        print(adj)           
        ans = 1
        for i in range(n):
            cnt = 1
            stack = [i]
            vis = set([i])
            while stack:
                v = stack.pop()
                for u in adj[v]:
                    if not u in vis:
                        cnt += 1
                        stack.append(u)
                        vis.add(u)
            ans = max(ans, cnt)
                
        return ans
        