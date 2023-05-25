class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for i in range(len(sentences)):
            new_list = sentences[i].split(" ")
            count = len(new_list)
            if count > ans:
                ans = count
        return ans