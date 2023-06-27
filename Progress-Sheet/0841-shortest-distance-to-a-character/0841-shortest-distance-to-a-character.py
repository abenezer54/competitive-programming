class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        arr = [char for char in s]
        print(arr)
        idx = []
        for i, j in enumerate(arr):
            if j == c:
                idx.append(i)
        j = 0 #to count the index of the c
        ans = []
        for i in range(len(arr)):
            if s[i] == c:
                ans.append(0)
                j += 1
            elif i < idx[0]:
                ans.append(idx[0] - i)
            elif i > idx[-1]:
                ans.append(i - idx[-1])
            else:
                ans.append(min((i - idx[j - 1]), (idx[j] - i)))
        return ans