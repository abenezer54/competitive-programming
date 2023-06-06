class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedWords = []
        for word in strs:
            arr = sorted([x for x in word])
            sortedWords.append(arr)

        dic = {}
        for i in range(len(sortedWords)):
            if "".join(sortedWords[i]) in dic:
                dic["".join(sortedWords[i])].append(i)
            else:
                dic["".join(sortedWords[i])] = [i] 
                
        temp = []
        for value in dic.values():
            temp.append(value)

        for i in range(len(temp)):
            for j in range(len(temp[i])):
                idx = temp[i][j]
                temp[i][j] = strs[idx] 

        return temp