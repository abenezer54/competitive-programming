class TrieNode:
    def __init__(self):
        self.child = {}
        self.ie = False

class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = TrieNode()
            cur = cur.child[ch]
        cur.ie = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if ch not in cur.child:
                return False
            cur = cur.child[ch]
        return cur.ie
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            if ch not in cur.child:
                return False
            cur = cur.child[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)