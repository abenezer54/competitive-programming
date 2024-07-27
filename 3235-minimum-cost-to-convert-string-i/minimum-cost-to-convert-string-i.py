class Solution:
    def minimumCost(self, s: str, t: str, o: List[str], c: List[str], cost: List[int]) -> int:
        n, m = len(s), len(o)
        adj = defaultdict(list)
        mn = defaultdict(lambda: float('inf'))
        for i in range(m):
            mn[(o[i], c[i])] = min(mn[(o[i], c[i])], cost[i])

        for key, val in mn.items():
            adj[key[0]].append((key[1], val))


        min_cost = defaultdict(lambda: float('inf'))
        for i in range(26):
            char = chr(i + 97)
            heap = [(0, char)]
            vis = set()
            while heap:
                w, node = heapq.heappop(heap)
                if node in vis:
                    continue
                vis.add(node)
                min_cost[(char, node)] = w
                for nei, wi in adj[node]:
                    heapq.heappush(heap, (w + wi, nei))

        ans = 0
        for i in range(n):
            if (s[i], t[i]) not in min_cost:
                return -1
            ans += min_cost[(s[i], t[i])]
            
        return ans
