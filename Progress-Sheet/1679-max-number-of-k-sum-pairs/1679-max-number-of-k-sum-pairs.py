class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        count = 0
        for num in nums:
            comp = k - num
            if counter[comp] > 0:
                counter[comp] -= 1
                count += 1
            else:
                counter[num] += 1
        return count