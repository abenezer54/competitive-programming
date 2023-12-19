class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [num + 1 for num in range(n)]
        lossers = set()
        pointer = 0
        for _ in range(n - 1):
            count = 0
            while count < k:
                if players[pointer % n] not in lossers:
                    count += 1
                pointer += 1
            lossers.add(players[pointer % n - 1])

        for player in players:
            if player not in lossers:
                return player