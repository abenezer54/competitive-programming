class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mp = {e.id:e for e in employees}
        stack = [mp[id]]
        ans = 0
        while stack:
            top = stack.pop()
            ans += top.importance
            for node in top.subordinates:
                stack.append(mp[node])
        return ans
        