class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementSum = sum(nums)
        arr1 = []
        for i in nums:
            if len(str(i)) > 1:
                arr = list(map(int, [x for x in str(i)]))
                i = sum(arr)
                arr1.append(i)
            else:
                arr1.append(i)
        digitSum = sum(arr1)
        return abs(elementSum - digitSum)