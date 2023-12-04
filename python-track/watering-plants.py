class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        c = capacity 
        ans = 0
        for i in range(len(plants)):
            if c >= plants[i]:
                ans += 1
                c -= plants[i]
            else:
                c = capacity
                ans += i + i + 1
                c -= plants[i]
        return ans
        