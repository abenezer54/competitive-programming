class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxx = max(trips, key = lambda x: x[-1])[-1]
        people = [0] * (maxx + 2) #Number of passangers in each location

        for passengers, start, final in trips:
            people[start] += passengers
            people[final] -= passengers

        for i in range(maxx + 2):
            if i > 0:
                people[i] += people[i - 1]
            if people[i] > capacity:
                return False
        
        return True          
        