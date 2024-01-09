class Solution:
    def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
        ans = []
        p1 = p2 = 0
        while p1 < len(first) and p2 < len(second):
            l = max(first[p1][0], second[p2][0])
            r = min(first[p1][1], second[p2][1])
            if l <= r:
                ans.append([l, r])
            if first[p1][1] < second[p2][1]:
                p1 += 1
            else:
                p2 += 1
        return ans
