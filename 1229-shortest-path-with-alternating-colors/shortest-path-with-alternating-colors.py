class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        adjred = [[] for _ in range(n)]
        adjblue = [[] for _ in range(n)]

        for u, v in redEdges:
            adjred[u].append((v, 0))
        for u, v in blueEdges:
            adjblue[u].append((v, 1))

        ans = [-1] * n
        que = deque([(0, -1)])
        vis, length = set(), 0
        while que:
            l = len(que)
            for _ in range(l):
                node, prev = que.popleft()
                if ans[node] == -1:
                    ans[node] = length

                if prev == -1 or prev == 1:
                    for child in adjred[node]:
                        if child not in vis:
                            que.append(child)
                            vis.add(child)
                if prev == -1 or prev == 0:
                    for child in adjblue[node]:
                        if child not in vis:
                            que.append(child)
                            vis.add(child)
            length += 1
        return ans
