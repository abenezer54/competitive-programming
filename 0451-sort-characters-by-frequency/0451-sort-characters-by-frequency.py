class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        temp = []
        for key, value in dic.items():
            temp.append([key, value])
        print(temp)
        
        for i in range(len(temp)):
            max_index = i
            for j in range(i +1, len(temp)):
                if temp[j][1] > temp[max_index][1]:
                    max_index = j
            temp[i], temp[max_index] = temp[max_index], temp[i]
        print(temp)
        ans = ""
        for i, j in temp:
            ans += i * j
        return ans
#         from collections import defaultdict
#         arr = [x for x in s]
#         dic = defaultdict(int)
#         for i in arr:
#             dic[i] += 1
#         print(dic)
#         frequency = []
#         for i in dic.values():
#             frequency.append(i)
#         frequency.sort(reverse = True)
#         print(frequency)
#         ans = ""
#         for i in frequency:
#             value = [x for x in dic if dic[x]== i]
#             if len(value) == 1:
#                 ans += "".join(map(str,value)) *i
#             else:
#                 j = 0
#                 while(j < len(value)-1):
#                     ans += value[j] * i
#                     j += 1
#             print(ans)
            
        
            