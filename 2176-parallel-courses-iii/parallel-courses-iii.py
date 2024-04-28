class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        mx = defaultdict(int)
        adj = [[] for _ in range(n + 1)]
        ind = [0] * (n + 1)

        for a, b in relations:
            adj[a].append(b)
            ind[b] += 1
        
        ans = 0
        que = deque()
        for i in range(1, n + 1):
            if not ind[i]:
                ans = max(ans, time[i - 1])
                que.append((i, time[i - 1]))

        while que:
            l = len(que)
            for _ in range(l):
                node, prev = que.popleft()

                for child in adj[node]:
                    mx[child] = max(mx[child], prev)
                    ind[child] -= 1
                    if not ind[child]:
                        ans = max(ans,  mx[child] + time[child - 1])
                        que.append((child, mx[child] + time[child - 1]))
        return ans

        