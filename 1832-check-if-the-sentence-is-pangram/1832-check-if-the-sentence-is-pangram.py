class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set(sentence)
        return len(s) == 26