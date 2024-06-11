class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = set(arr2)
        a, b = [], []
        for num in arr1:
            if num in c:
                a.append(num)
            else:
                b.append(num)
        mp = {arr2[i]: i for i in range(len(arr2))}
        a.sort(key=lambda item: mp[item])
        b.sort()
        return a + b