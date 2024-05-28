class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.ie = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.root.ie = True


    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not cur.child[idx]:
                cur.child[idx] = TrieNode()
            cur = cur.child[idx]
        cur.ie = True    

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)

        stk = [(trie.root, 0)]
        vis = set([trie.root])
        p, mp = {}, {}
        maxx = 0
        last_node = None
        while stk:
            node, l = stk.pop()
            is_last = True
            for idx in range(25, -1, -1):
                if node.child[idx] and node.child[idx].ie and node.child[idx] not in vis:
                    p[node.child[idx]] = node
                    mp[node.child[idx]] = chr(97 + idx)
                    is_last = False
                    stk.append((node.child[idx], l + 1))
                    vis.add(node.child[idx])
            if is_last and l > maxx:
                maxx = l
                last_node = node
                
        cur = last_node
        ans = []
        while cur in p:
            ans.append(mp[cur])
            cur = p[cur]
        return ''.join(ans[::-1])
                        

