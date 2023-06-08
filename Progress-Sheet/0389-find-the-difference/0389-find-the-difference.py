class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        arr1 = sorted([x for x in s])
        arr2 = sorted([x for x in t])
        for i in range(len(s)):
            if arr1[i] != arr2[i]:
                return arr2[i]
        return arr2[-1]
            