class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        dic = {}
        l = 0
        r = len(skill) - 1
        while l < r:
            if not (skill[l] + skill[r]) in dic:
                dic[skill[l] + skill[r]] = [[skill[l], skill[r]]]
            else:
                dic[skill[l] + skill[r]].append([skill[l], skill[r]])
            l += 1
            r -= 1

        temp = [[x, y] for x, y in dic.items()]

        if len(temp) == 1:
            ans = 0
            for i in range(len(temp[0][1])):
                ans += temp[0][1][i][0] * temp[0][1][i][1]
            return ans
        return -1
