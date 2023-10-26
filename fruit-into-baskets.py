class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        N = len(fruits)
        dic = {}
        ans = 0
        l = 0
        for r, fruit in enumerate(fruits):
            if fruit not in dic:
                dic[fruit] = 1
            else:
                dic[fruit] += 1
            while len(dic) > 2:
                dic[fruits[l]] -= 1
                if dic[fruits[l]] == 0:
                    del dic[fruits[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans