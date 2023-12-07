class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = defaultdict(int)
        losers = defaultdict(int)
        for winner, loser in matches:
            winners[winner] += 1
            losers[loser] += 1

        ans = [[], []]
        for key, value in winners.items():
            if key not in losers:
                ans[0].append(key)
        for key, value in losers.items():
            if value == 1:
                ans[1].append(key)
        
        ans[0].sort()
        ans[1].sort()
        
        return ans

        