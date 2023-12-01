class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {order[i]: i for i in range(26)}
        for i in range(len(words) - 1):
            equal = True
            check = zip(words[i], words[i+1])
            for a, b in check:
                if dic[a] != dic[b]:
                    equal = False
                if dic[a] > dic[b]:
                    return False
                elif dic[a] < dic[b]:
                    break   
            if equal and len(words[i]) > len(words[i+1]):
                return False
        return True
            