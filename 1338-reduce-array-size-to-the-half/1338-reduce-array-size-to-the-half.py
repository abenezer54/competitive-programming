from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)//2
        dic = Counter(arr)
        temp = []
        for key, value in dic.items():
            temp.append([key, value])
        temp.sort(key = lambda x: x[1], reverse = True)
        print(temp)
        count = 0
        x = 0
        for i in temp:
            if i[1] + x < n:
                x += i[1]
                count += 1
            elif i[1] + x >= n:
                count += 1
                break

        
        return count