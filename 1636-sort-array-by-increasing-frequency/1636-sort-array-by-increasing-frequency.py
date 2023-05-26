from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)
        print(dic)
        arr = []
        for key, value in dic.items():
            arr.append([key, value])
        print(arr)
        arr.sort(key = lambda x:(x[1], -x[0] ))
        print(arr)
        ans = []
        for i, j in arr:
            ans.extend([i]*j)
        return ans
            
        