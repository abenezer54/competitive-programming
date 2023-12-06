class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        ans = []
        for key, value in count.items():
            if value > len(nums)//3:
                ans.append(key)

        return ans
        