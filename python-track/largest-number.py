class Largest(str):
    def __lt__( x, y):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(key=Largest)
        if nums[0] == "0":
            return "0"

        return "".join(nums)
        