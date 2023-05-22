class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split()
        reversedArr = []
        for i in arr:
            reversedArr.append(i[::-1])
        reversedArr.sort()
        arr2 = []
        for i in reversedArr:
            arr2.append(i[:0:-1])
        res = " ".join(arr2)  
        return res
