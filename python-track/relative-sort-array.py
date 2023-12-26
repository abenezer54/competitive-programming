class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        look = {arr2[i]: i for i in range(len(arr2))}
        return sorted(arr1, key = lambda x: (look.get(x, float("inf")), x))