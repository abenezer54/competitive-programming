class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic= {}
        for i in s:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        print(dic)
        ans = ''
        for x in order:
            if x in s:
                ans += x*dic[x]

        for y in s:
            if y not in ans:
                ans += y*dic[y]
        return ans