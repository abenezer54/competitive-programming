class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        repeated = set()
        for front, back in zip(fronts, backs):
            if front == back:
                repeated.add(front)
        print(repeated)
        possible = set()
        for front, back in zip(fronts, backs):
            if front not in repeated:
                possible.add(front)
            if back not in repeated:
                possible.add(back)
      
        if not possible:
            return 0

        return min(possible)
        