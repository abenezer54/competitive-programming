class Solution:
    def isNStraightHand(self, hand: List[int], size: int) -> bool:
        n = len(hand)
        if n % size:
            return False
        c = Counter(hand)
        a = sorted(list(set(hand)))
        for i in range(len(a)):
            if c[a[i]] > 0:
                temp = c[a[i]]
                for num in range(a[i], a[i] + size):
                    if c[num] < temp:
                        return False
                    c[num] -= temp
                c[a[i]] -= 1
        return True
        