class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        ans = []
        for word in words:
            check = []
            for i in range(len(word)):
                if word[i].lower() in row1:
                    check.append(1)
                elif word[i].lower() in row2:
                    check.append(2)
                else:
                    check.append(3)
            if all([check[0] == c for c in check]):
                ans.append(word)
        return ans        