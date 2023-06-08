class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        dic = Counter(s)
        print(dic)
        if letter not in dic:
            return 0
        else:
            return dic[letter]* 100 // len(s) 