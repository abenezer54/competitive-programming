class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        nums.sort(reverse=True)
        nums.sort(key=lambda x:cnt[x])
        return nums
        