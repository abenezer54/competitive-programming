from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:

        dic = Counter(s)
        temp = []
        for key, value in dic.items():
            temp.append([key, value])
        print(temp)
        temp.sort(key = lambda x : x[1], reverse=True)

        print(temp)
        ans = ""
        for i, j in temp:
            ans += i * j
        return ans

            
        
            
