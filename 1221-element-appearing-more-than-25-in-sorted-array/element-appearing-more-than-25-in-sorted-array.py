class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = Counter(arr)
        maxx = max(count.values())
        for key, val in count.items():
            if val == maxx:
                return key
        
        