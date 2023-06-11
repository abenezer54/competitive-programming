class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxx = max(nums)
        minn = min(nums)
        r = maxx - minn + 1
        counter = [0] * r
        for i in range(len(nums)):
            counter[nums[i] -minn] += 1

        sortedarr = []
        for i in range(r):
            while counter[i] > 0:
                sortedarr.append(i + minn)
                counter[i] -= 1

        return sortedarr[-k]