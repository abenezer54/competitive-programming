class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        total = skill[0] + skill[-1]
        ans = 0
        n = len(skill)
        for i in range(n // 2):
            cur_sum = skill[i] + skill[~i]
            if cur_sum != total:
                return -1
            ans += skill[i] * skill[~i]

        return ans
        