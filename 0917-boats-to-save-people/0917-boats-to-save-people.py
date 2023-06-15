class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        if len(people) == 1:
            return 1
        else:
            ans = 0
            l = 0
            r = len(people) - 1
            while l <= r:
                if people[l] + people[r] <= limit:
                    l += 1
                    r -= 1
                else:
                    r -= 1  
                ans += 1           
            return ans       