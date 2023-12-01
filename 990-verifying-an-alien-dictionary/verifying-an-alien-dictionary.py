class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words) - 1):
            equal = True
            for j in range(min(len(words[i]), len(words[i+1]))):
                i1 = order.index(words[i][j])
                i2 = order.index(words[i+1][j])
                if i1 != i2:
                    equal = False
                if i1 > i2:
                    return False
                elif i1 < i2:
                    break   
            if equal and len(words[i]) > len(words[i+1]):
                return False
        return True
            