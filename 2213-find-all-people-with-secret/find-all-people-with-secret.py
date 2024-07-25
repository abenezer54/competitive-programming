class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        ans = set([0, firstPerson])
        mp = {}

        for x, y, t in meetings:
            if t not in mp:
                mp[t] = defaultdict(list)
            mp[t][x].append(y)
            mp[t][y].append(x)

        def dfs(node, adj):
            if node in vis:
                return 
            vis.add(node)
            ans.add(node)
            for nei in adj[node]:
                dfs(nei, adj)
        
        for t in sorted(mp.keys()):
            vis = set()
            for node in mp[t]:
                if node in ans:
                    dfs(node, mp[t])
                    
        return list(ans)
        