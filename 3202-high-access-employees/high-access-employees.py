class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        dic = defaultdict(list)
        for name, time in access_times:
            if int(time) != 5 and int(time) != 2350:
                dic[name].append(int(time))
        ans = []
        for key, value in dic.items():
            if len(value) >= 3:
                temp = sorted(value)
                for i in range(len(temp) - 2):
                    if temp[i+2] - temp[i] < 100:
                        ans.append(key)
                        break
            else:
                continue
        print(dic)       
        return ans
        