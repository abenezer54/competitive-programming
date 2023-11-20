class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        ans = p = 0
        for t in trainers:
            if p < len(players) and players[p] <= t:
                ans += 1
                p += 1
        return ans
        