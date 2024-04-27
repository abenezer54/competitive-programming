class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        n, s = len(board), pow(len(board), 2) 
        arr = []
        for i in range(n):
            if i & 1:
                arr.extend(board[i][::-1])
            else:
                arr.extend(board[i][:])

        que = deque([1])
        vis = set([1])
        move = 0
        while que:
            l = len(que)
            for _ in range(l):
                node = que.popleft()

                if node == s: return move
                for child in range(node + 1, min(node + 7, s + 1)):
                    nxt = child
                    if arr[child - 1] != -1:
                        nxt = arr[child - 1]
                    if nxt not in vis:
                        que.append(nxt)
                        vis.add(nxt)
            move += 1
        return -1
