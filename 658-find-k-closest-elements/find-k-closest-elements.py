class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = [(abs(num - x), num) for num in arr]
        heapify(heap)
        return sorted([num for d, num in nsmallest(k, heap)])
        