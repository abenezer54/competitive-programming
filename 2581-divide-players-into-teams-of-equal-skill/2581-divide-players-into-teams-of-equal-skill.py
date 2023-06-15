class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        ans = 0
        skill.sort()
        l = 0
        r = len(skill) - 1
        x = skill[l] + skill[r]

        while l < r:
            y = skill[l] + skill[r]
            if y != x:
                return -1
            else:
                ans += skill[l] * skill[r]
                l += 1
                r -=1
        
        return ans
        