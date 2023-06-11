class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = []
        loserCounter = Counter()

        for match in matches:
            winners.append(match[0])
            loserCounter[match[1]] += 1

        ans1 = set()
        ans2 = []

        for winner in winners:
            if winner not in loserCounter:
                ans1.add(winner)

        for loser, count in loserCounter.items():
            if count == 1:
                ans2.append(loser)

        ans3 = sorted(list(ans1))
        ans2.sort()

        return [ans3, ans2]
