class Trie:

    def __init__(self):
        self.root = [None] * 27


    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not cur[idx]:
                cur[idx] = [None] * 27
            cur = cur[idx]
        cur[-1] = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not cur[idx]:
                return False
            cur = cur[idx]
        return cur[-1]
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not cur[idx]:
                return False
            cur = cur[idx]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)