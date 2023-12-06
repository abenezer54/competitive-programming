class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)

        ans = []
        for i in range(len(positives)):
            ans.extend([positives[i], negatives[i]])

        return ans
        