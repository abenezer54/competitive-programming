class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d = deque()
        r = deque()
        n = len(senate)
        for i in range(n):
            if senate[i] == "R":
                r.append(i)
            else:
                d.append(i)
        
        while True:
            if not d:
                return "Radiant"
            if not r:
                return "Dire"
            if d.popleft() < r.popleft():
                d.append(n)
            else:
                r.append(n) 
            n += 1
    
        