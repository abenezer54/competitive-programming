class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        heap = [(-val, key) for key, val in cnt.items()]
        heapify(heap)
        return [key for val, key in nsmallest(k, heap)]
        