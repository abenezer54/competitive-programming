class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        fastestGhost = float("inf")
        
        for x, y in ghosts:
            distance = abs(target[0] - x) + abs(target[1] - y)
            fastestGhost = min(fastestGhost, distance)
        myDistance = abs(target[0]) + abs(target[1])

        return myDistance < fastestGhost    