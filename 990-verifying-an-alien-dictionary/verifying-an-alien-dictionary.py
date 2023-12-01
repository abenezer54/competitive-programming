class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words) - 1):
            equal = True
            for j in range(min(len(words[i]), len(words[i+1]))):
                if order.index(words[i][j]) != order.index(words[i+1][j]):
                    equal = False
                if order.index(words[i][j]) > order.index(words[i+1][j]):
                    return False
                elif order.index(words[i][j]) < order.index(words[i+1][j]):
                    break
                
            if equal and len(words[i]) > len(words[i+1]):
                return False
        return True
            