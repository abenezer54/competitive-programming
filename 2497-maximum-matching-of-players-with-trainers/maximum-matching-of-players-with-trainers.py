class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        trainers.sort()
        players.sort()
        j = ans = 0

        for i in range(len(players)):
            while j < len(trainers) and players[i] > trainers[j]:
                j += 1
            if j < len(trainers):
                ans += 1
                j += 1
        return ans
