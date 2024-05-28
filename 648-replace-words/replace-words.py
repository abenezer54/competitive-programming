class Trie:

    def __init__(self):
        self.root = {}


    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['*'] = {}

    def search(self, word: str) -> bool:
        cur = self.root
        for i, ch in enumerate(word):
            if ch not in cur:
                return word
            cur = cur[ch]
            if '*' in cur:
                return word[:i + 1]
        return word
    

class Solution:
    def replaceWords(self, dictionary: List[str], s: str) -> str:
        s = s.split()
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        for i in range(len(s)):
            s[i] = trie.search(s[i])
        return ' '.join(s) 
        