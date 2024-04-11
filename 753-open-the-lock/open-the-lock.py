class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def nxt(x):
                if x == 10: return 0
                if x == -1: return 9
                return x

        def generate_child(cur):     
            cur = list(cur)    
            childs = []
            for i in range(4):
                new = cur[:]
                new[i] = str(nxt(int(new[i]) + 1))
                childs.append(''.join(new))
                new2 = cur[:]
                new2[i] = str(nxt(int(new2[i]) - 1))
                childs.append(''.join(new2))
            return childs

        deadends = set(deadends)
        vis = set([target])
        que = deque([target])
        turn = 0
        while que:
            l = len(que)
            for _ in range(l):
                node = que.popleft()
                if node == '0000': return turn
                for child in generate_child(node):
                    if child not in deadends and child not in vis:
                        que.append(child)
                        vis.add(child)
            turn += 1

        return -1
        