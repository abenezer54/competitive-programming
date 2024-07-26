class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = [[] for _ in range(n)]
        for src, dst, w in edges:
            adj[src].append((dst, w))
            adj[dst].append((src, w))
        ans = 0
        mn = float('inf')

        for v in range(n): # Do Djkstra to every node to find nei at threshold distance
            cnt = 0
            heap = [(0, v)]
            vis = set()
            while heap:
                prev, node = heapq.heappop(heap)
                if node in vis:
                    continue
                vis.add(node)
                for nei, w in adj[node]:
                    if prev + w <= distanceThreshold:
                        heapq.heappush(heap, (prev + w, nei))
            if len(vis) - 1 <= mn:
                mn = len(vis) - 1
                ans = v
                
        return ans