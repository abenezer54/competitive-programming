class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        ans = 0
        for word in words:
            cur = Counter(word)
            f = False
            for k, v in cur.items():
                if v > count[k]:
                    f = True
                    break
            if not f:
                ans += len(word)
        return ans
        