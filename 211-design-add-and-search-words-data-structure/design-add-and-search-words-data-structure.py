class WordDictionary:

    def __init__(self):
        self.root = {}
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur["*"] = {}
        

    def search(self, word: str) -> bool:
        n = len(word)
        def find(i, cur):
            if i == n - 1:   
                if word[i] == '.':
                    final = False
                    for node in cur.values():
                        if "*" in node:
                            final = True
                    return final
                else:
                    if word[i] in cur:
                        return "*" in cur[word[i]]
                    return False
            if word[i] == '.':
                final = False
                for node in cur.values():
                    if find(i + 1, node):
                        final = True
                return final
            else:
                if word[i] not in cur:
                    return False
                return find(i + 1, cur[word[i]])

        return find(0, self.root)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)