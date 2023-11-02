class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        s = set()
        for num in range(left, right + 1):
            s.add(num)

        domain = set()
        for row in ranges:
            for num in range(row[0], row[1] + 1):
                domain.add(num)
                
        for num in s:
            if not num in domain:
                return False
        
        return True