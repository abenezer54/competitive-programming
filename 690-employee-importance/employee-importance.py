"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], idd: int) -> int:
        adj = defaultdict(list)
        imp = Counter()
        for e in employees:
            adj[e.id] = e.subordinates
            imp[e.id] = e.importance

        stack = [idd]
        tot = 0
        while stack:
            top = stack.pop()
            tot += imp[top]
            for node in adj[top]:
                stack.append(node)
                
        return tot
        