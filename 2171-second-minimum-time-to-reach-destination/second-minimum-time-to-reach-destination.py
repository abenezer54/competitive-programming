class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = defaultdict(list)
        m = len(edges)
        for i in range(m):
            adj[edges[i][0]].append(edges[i][1])
            adj[edges[i][1]].append(edges[i][0])
        d1 = [float("inf")] * (n + 1)
        d2 = [float("inf")] * (n + 1)
        freq = [0] * (n + 1)

        heap = [(0, 1)]
        d1[1] = 0
        while heap:
            t, node = heapq.heappop(heap)
            freq[node] += 1

            if freq[node] == 2 and node == n: return t
            if (t // change) % 2:
                t = (change * (t // change + 1)) + time
            else:
                t += time
            
            for nei in adj[node]:
                if freq[nei] == 2:
                    continue
                
                if d1[nei] > t:
                    d2[nei] = d1[nei]
                    d1[nei] = t
                    heappush(heap, (t, nei))
                elif d2[nei] > t and d1[nei] != t:
                    d2[nei] = t
                    heappush(heap, (t, nei))
                    
        return d2[-1]
        