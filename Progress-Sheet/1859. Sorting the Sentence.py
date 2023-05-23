class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split()
        sortedArr = sorted(arr, key = lambda x: x[-1])
        return " ".join(i[:-1] for i in sortedArr)
